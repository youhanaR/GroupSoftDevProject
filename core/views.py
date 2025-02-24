# Author: Ameera Abdullah, Juri Khushayl

from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UserUpdateForm, UserDeleteForm
from .models import Location
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Landing Page View
def landing_page(request):
    return render(request, 'landing.html')

# User Sign Up View
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid(): # Validate the form 
            try:
                form.save() # Save the form 
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('my-login')  # Redirect to login page
            except IntegrityError:
                messages.error(request, "Username already exists. Please choose another one.")
    # Allows to access the form in the html file by {{ registerform }}
    context = {'registerform': form}  
    return render(request, 'register.html', context=context)

# User Login View
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid(): # validate the form
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password) # Checks for correct credentials
            if user is not None:
                auth.login(request, user) # Log the user in after authentication
                return redirect("dashboard")  # Redirect to the dashboard after login
    # Allows to access the form in the html file by {{ form }}
    context = {'loginform': form}
    return render(request, 'my-login.html', context=context)

# Main Page View (Dashboard)
def dashboard(request):
    locations = Location.objects.all()  # Get all locations from the database
    return render(request, 'dashboard.html', {'locations': locations})  # Pass locations to the template

# Log Out View
def user_logout(request):
    auth.logout(request) # log out the user then remove authentication credentials
    return render(request, 'user-logout.html')


# User Profile 
@login_required(login_url='my-login') # Allowed for logged in users 
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid(): # Validate the updated form
            u_form.save() # save the updated form
    else:
        u_form = UserUpdateForm(instance=request.user)
    # Allows to access the form in the html file by {{ u_form }}
    context = {'u_form': u_form,}
    return render(request, 'user-profile.html', context=context)


# User Update 
@login_required(login_url='my-login') # Allowed for logged in users 
def deleteAccount(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user # Get the logged user
        user.delete() # Delete the user 
        return redirect('landing')
    else:
        delete_form = UserDeleteForm(instance=request.user)
    context = {'delete_form': delete_form}
    return render(request, 'delete-account.html', context=context)



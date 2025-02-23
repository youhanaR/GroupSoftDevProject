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
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('my-login')  # Redirect to login page
            except IntegrityError:
                messages.error(request, "Username already exists. Please choose another one.")
    
    context = {'registerform': form}  
    return render(request, 'register.html', context=context)

# User Login View
def my_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")  # Redirect to the dashboard after login
    
    context = {'loginform': form}
    return render(request, 'my-login.html', context=context)

# Main Page View (Dashboard)
def dashboard(request):
    locations = Location.objects.all()  # Get all locations from the database
    return render(request, 'dashboard.html', {'locations': locations})  # Pass locations to the template

# Log Out View
def user_logout(request):
    auth.logout(request)
    return render(request, 'user-logout.html')



# update user profile
@login_required(login_url='my-login')
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {'u_form': u_form,}
    return render(request, 'user-profile.html', context=context)


@login_required(login_url='my-login')
def deleteAccount(request):
    if request.method == 'POST':
        
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('landing')
    
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {'delete_form': delete_form}

    return render(request, 'delete-account.html', context=context)



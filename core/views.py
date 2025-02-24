from django_email_verification import send_email

from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from .models import Location

from django.contrib import messages
from django.db import IntegrityError

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


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
            
            form.save(commit=False)
            user_email = form.cleaned_data['email']
            user_username = form.cleaned_data['username']
            user_password = form.cleaned_data['password1']

            # Create new user
            user = User.objects.create_user(username=user_username, email=user_email, password=user_password)

            # Make user unactive until they click link to token in email
            user.is_active = False 
            send_email(user)
                
            return HttpResponseRedirect(reverse('my-login'))
            
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
    return redirect('landing')



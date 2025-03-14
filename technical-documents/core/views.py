# Author: Juri Kushayi, Surin Chai, Ameera Abdullah, Jem Challis

"""
This module defines the views for the Django web application. For this prototype, 
it handles user authentication, game descriptions, and dashboard navigation.

Views:
--------
1. **Landing Page** (`landing_page`) - Displays the main landing page of the website.
2. **User Authentication**:
   - `register` - Handles user registration.
   - `my_login` - Manages user login authentication.
   - `user_logout` - Logs out the user and redirects to a logout page.
3. **Dashboard & User Management**:
   - `dashboard` - Displays an interactive map with game locations.
   - `user_profile` - Allows users to update their profile details.
   - `deleteAccount` - Enables users to delete their account.
4. **Game Descriptions** (`game_description`) - Displays an overview of the game based on the selected location.

Author: Juri Khushayl, Surin Wi Sut, Ameera Abdullah, Jem Challis
"""

from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UserUpdateForm, UserDeleteForm
from .models import Location
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound

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



# Update user profile
@login_required(login_url='my-login')
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

#Renders a game description page based on the selected location.
def game_description(request, location):
    # Normalize the location string to match dictionary keys
    normalized_location = location.lower().replace(" ", "-")
    game_url = (Location.objects.get(name=location)).game.url

    # Hardcoded game data
    game_data = {
    'into-building': {
        'title': 'Match 3',
        'description': 'Match different types of waste to learn how to properly dispose of them.',
        'how_to_play': 'Click on matching waste items to clear them from the board. Try to reach the highest score before the time runs out!',
        'sustainability_theme': 'Reducing landfill waste starts with small actions—<a href="https://www.exeter.ac.uk/about/sustainability/whatyoucando/" target="_blank">each one adds up to a cleaner world!</a>',
    },
    'cornwall-house': {
        'title': 'Recycle Rush',
        'description': 'Sort recyclable materials as fast as you can before time runs out!',
        'how_to_play': 'Drag and drop each item into the correct recycling bin. The faster you sort, the higher your score!',
        'sustainability_theme': 'Toss it right for a greener sight<a href="https://www.exeter.ac.uk/about/sustainability/whatyoucando/" target="_blank">—every action counts in saving our Earth!</a>',
    },
    'sports-park': {
        'title': 'Under Construction',
        'description': '',
        'how_to_play': '',
        'sustainability_theme': '',
    },
}


    # Retrieve the data for the given location
    game_info = game_data.get(normalized_location)

    # If location is invalid, return a 404 page
    if not game_info:
        return HttpResponseNotFound("<h1>Game description not found</h1>")

    return render(request, 'game_description.html', {
        'game_title': game_info['title'],
        'game_description': game_info['description'],
        'how_to_play': game_info['how_to_play'],
        'sustainability_theme': game_info['sustainability_theme'],
        'location': normalized_location,
        'game_url': game_url
    })
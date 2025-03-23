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
   - `privacy_policy` - Content of privacy policy that is dynamically accessed by the registration page.
3. **Dashboard & User Management**:
   - `dashboard` - Displays an interactive map with game locations.
   - `user_profile` - Allows users to update their profile details.
   - `deleteAccount` - Enables users to delete their account.
4. **Game Descriptions** (`game_description`) - Displays an overview of the game based on the selected location.

Author: Juri Khushayl, Surin Wi Sut, Ameera Abdullah
"""

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, UserUpdateForm, UserDeleteForm
from .models import Location
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound
from django.urls import reverse


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

#Privacy Policy Pop-Up Content
def privacy_policy(request):
    return render(request, 'privacy_policy.html')

# Main Page View (Dashboard)
def dashboard(request):
    locations = Location.objects.all()  # Get all locations from the database
    return render(request, 'dashboard.html', {'locations': locations})  # Pass locations to the template

#leaderboard view
def leaderboard(request):
    return render(request, 'leaderboard.html')

#how to play view
def how_to_play(request):
    return render(request, 'how_to_play.html')

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
 
    normalized_location = location.lower().replace(" ", "-")
    location_obj = get_object_or_404(Location, name=location)

    # Retrieve the minigame URL using the new field if it exists
    if location_obj.minigame and location_obj.minigame.intro_url_name:
        game_url = reverse(location_obj.minigame.intro_url_name)
    else:
        game_url = None

    # Hardcoded game data
    game_data = {
        'into-building': {
            'title': 'Sort the Recycling',
            'sustainability_theme': 'Sorting recycling correctly reduces contamination, ensuring that more materials can be reused and kept out of landfills.This game teaches you to sort materials correctly and underscores how<a href="https://www.exeter.ac.uk/about/sustainability/whatyoucando/" target="_blank">small actions can lead to big effects!</a>',
        },
        'cornwall-house': {
            'title': 'Recycle Rush',
            'sustainability_theme': 'Recycling helps reduce waste, conserve natural resources, and minimise pollution. By playing this game, you learn the importance of sorting waste properly and how <a href="https://www.exeter.ac.uk/about/sustainability/whatyoucando/" target="_blank">small actions can contribute the a sustainable future!</a>',
        },
        'sports-park': {
            'title': 'Trash Trivia',
            'sustainability_theme': '',
        },
        'forum': {
            'title': 'Whack-A-Waste',
            'sustainability_theme': 'Reducing food waste helps conserve resources and lower environmental impact. This game puts your food-saving skills to the test! Learn how to rescue, reuse, and <a href="https://www.exeter.ac.uk/about/sustainability/whatyoucando/" target="_blank">rethink food at every stage of its shelf life to cut down on waste and help the planet.</a>',
        },
        'business-school-cafe': {
            'title': 'Sort-n-Serve',
            'sustainability_theme': '',
        },
        'reed-pond': {
            'title': 'Sea Sweepers',
            'sustainability_theme': 'Reducing waste in our waters helps protect marine life and preserve ecosystems. This game challenges you to clean up pollution from our waters and <a href="https://www.exeter.ac.uk/about/sustainability/whatyoucando/" target="_blank">learn how to reduce waste in bodies of water, ensuring a cleaner, healthier environment for all.</a>',
        },

    }

    # Retrieve the game info for the normalized location
    game_info = game_data.get(normalized_location)

    # If location is invalid, return a 404 page
    if not game_info:
        return HttpResponseNotFound("<h1>Game description not found</h1>")

    return render(request, 'game_description.html', {
        'game_title': game_info['title'],
        'sustainability_theme': game_info['sustainability_theme'],
        'location': normalized_location,
        'game_url': game_url
    })

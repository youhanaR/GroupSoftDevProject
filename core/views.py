from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, UserDeleteForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# import django authenticate models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# Landing Page View
# Welcome page for the applications
def landing_page(request):
    return render(request, 'landing.html')


# User Sign Up view
def register(request):
  # Create an empty CreateUserForm instance to display the form on the page
  form = CreateUserForm()
  
  if request.method == "POST": # Verify that the form has been submitted
      form = CreateUserForm(request.POST) # Attach the data that was submitted to the form
      if form.is_valid():  # Validate the form data
               form.save() # Save the new user to the database
               return redirect('my-login')  # Redirect to the login page after successful registration //  or redircet to the main page
    
   # Pass the form to the template for rendering     
  context = {'registerform': form}  
  return render(request, 'register.html', context=context)



# User Login View
def my_login(request):
     # Create an empty LoginForm instance to display the form on the page
    form = LoginForm()
    
    if request.method == 'POST': # Verify that the form has been submitted
        form = LoginForm(request, data=request.POST) # Attach the data that was submitted to the form
        
        if form.is_valid(): # Validate the form data
            # Take the password and username out of the data that was submitted
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # Authenticate the user using Django's built-in authenticate function
            user = authenticate(request, username=username, password=password) # authenticate() is used to check the username and password against the database.
            if user is not None: # If authentication is successful
                auth.login(request, user) # Log in the user
                # need to add a message to the show the login was successful
                return redirect("dashboard") # Redirect to the main page after login
    
    # Pass the form to the template for rendering
    context = {'loginform':form}
    return render(request, 'my-login.html', context=context)



# Main Page View
# Logout buttom
def dashboard(request):
    # displays the main page to users who have been authenticated.
    return render(request, 'dashboard.html')


# Log Out View
def user_logout(request):
    # Logs out the user and ends their session
    auth.logout(request)
    # Redirect to the landing page after logout
    return render(request, 'user-logout.html')



# update user profile
@login_required(login_url='my-login')
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile') # Redirect back to profile page

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



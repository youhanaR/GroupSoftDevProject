from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms 
from .models import Profile

from django.forms.widgets import PasswordInput, TextInput
# - create a user (model form)

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1','password2']
        


# - authenticate a user   (model form)

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)
    
 
# Update user profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
       

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
    
    
    
# Author: Juri Khushayl

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms.widgets import PasswordInput, TextInput

# Sign up form for the user 
class CreateUserForm(UserCreationForm):
    agree = forms.BooleanField(
        required=True,
        label="I agree to the privacy policy"
    )
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

# Login form for the user 
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

# Update user profile form and validate method using (clean_fieldname) to check for duplicates in database table(User) 
class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()
        class Meta:
            model = User
            fields = ['username', 'email']
        
        def clean_username(self):
         username = self.cleaned_data.get('username')
         if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
                 raise forms.ValidationError('This username already exists.')
         return username
        
        def clean_email(self):
         email = self.cleaned_data.get('email')
         if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                 raise forms.ValidationError('This email already exists.')
         return email
            
# Delete user profile form 
class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
    
    
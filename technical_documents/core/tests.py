# Author: Surin Chai , Juri Khushayl

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django import forms



class RegisterTestCase(TestCase):
    def test_register_page(self):
        
        # Test if the sign up page loads successfully
        output = self.client.get(reverse('register'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'register.html')
        
    def test_register_successful(self):
        
        # Test if the user can register successfully
        test_data = {
            'username': 'usertesttest',
            'email': 'testtest@example.com',
            'password1': 'passwordtest1',
            'password2': 'passwordtest2',
        }
        
        output = self.client.post(reverse('register'), test_data)
        self.assertEqual(output.status_code, 302)  # This test failed 200 != 302 Not sure how to fix
        self.assertRedirects(output, reverse('my-login'))  
        self.assertTrue(get_user_model().objects.filter(username='usertesttest').exists())
        
    
class LoginTestCase(TestCase):
    def usertest(self):
        
        # Test user for login tests
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')
        
    def test_login_page(self):
        
        # Test load login page 
        output = self.client.get(reverse('my-login'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'my-login.html')
                                
    def test_login_successful(self):
        
        # Test successful login with correct login info
        testdata = {
            'username': 'testuseragain',
            'password': 'passwordtest1again'
        }
        output = self.client.post(reverse('my-login'), testdata)
        self.assertEqual(output.status_code, 302) # same error occurs as sign-in
        self.assertRedirects(output, reverse('home'))
        
class LandingPageTestCase(TestCase):
    
    def test_landing_page(self):
        
        # Test load landing page
        output = self.client.get(reverse('landing'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'landing.html')
        
class DashboardPageTestCase(TestCase):
    
    def test_dashboard_page(self):
        
        # Test load main page
        output = self.client.get(reverse('dashboard'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'dashboard.html')
        
class PasswordResetTestCase(TestCase):
    
    def test_password_reset_page(self):
        
        # Test load password reset page
        output = self.client.get(reverse('password_reset'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'password_reset.html')
        
class UserProfileTestCase(TestCase):
    
    def test_user_profile_page(self):
        
        # Test load user profile page
        output = self.client.get(reverse('user-profile'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'user-profile.html')
        
class UserLogoutTestCase(TestCase):
    
    def test_user_logout_page(self):
        
        # Test load user logout profile page
        output = self.client.get(reverse('user-logout'))
        self.assertEqual(output.status_code, 200) # same exact problem
        self.assertTemplateUsed(output, 'user-logout.html')
        

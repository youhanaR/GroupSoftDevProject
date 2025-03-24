# Author: Surin Chai , Juri Khushayl

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django import forms
from unittest.mock import patch
from core.models import Profile
from minigames.models import GameScore
from django.db import IntegrityError

class RegisterTestCase(TestCase):
    def test_register_page(self):
        self.client.logout()  # Ensure the user is logged out before starting the test
        output = self.client.get(reverse('register'))  # Access the register page
        self.assertEqual(output.status_code, 200)  # Ensure the page loads
        self.assertTemplateUsed(output, 'register.html')  # Ensure the correct template is used

    def test_register_successful(self):
        self.client.logout()  # Ensure the user is logged out before starting the test

        test_data = {
            'username': 'usertesttest',
            'email': 'testtest@example.com',
            'password1': 'passwordtest1',
            'password2': 'passwordtest2',
        }

        # Post data to simulate user registration
        output = self.client.post(reverse('register'), test_data)

        # Test if it redirects to the login page after registration
        self.assertEqual(output.status_code, 302)  # Expecting a redirect
        self.assertRedirects(output, reverse('my-login'))  # Should redirect to login page after successful registration

        # Check if the user was successfully created in the database
        self.assertTrue(get_user_model().objects.filter(username='usertesttest').exists())


        
class LoginTestCase(TestCase):
    def setUp(self):
        # Create a test user for login tests
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')

    def test_login_page(self):
        # Test that the login page is loading correctly
        output = self.client.get(reverse('my-login'))
        self.assertEqual(output.status_code, 200)
        self.assertTemplateUsed(output, 'my-login.html')

    def test_login_successful(self):
        # Test successful login with correct login info
        testdata = {
            'username': 'testuser',
            'password': 'password123'
        }
        output = self.client.post(reverse('my-login'), testdata)
        self.assertEqual(output.status_code, 302)  # Should redirect after successful login
        self.assertRedirects(output, reverse('dashboard'))  # Redirect to dashboard after login


class UserProfileTestCase(TestCase):
    def setUp(self):
        # Create a test user for the profile page test
        self.user = User.objects.create_user(username='testuser', password='password123', email='test@example.com')

    def test_user_profile_page(self):
        # Log in the user before accessing the profile page
        self.client.login(username='testuser', password='password123')

        # Request the user profile page
        output = self.client.get(reverse('user-profile'))

        # Check if the response is successful
        self.assertEqual(output.status_code, 200)  # Should be 200 since the user is logged in
        self.assertTemplateUsed(output, 'user-profile.html')  # Ensure the correct template is used

        
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
      
class UserLogoutTestCase(TestCase):
    
    def test_user_logout_page(self):
        
        # Test load user logout profile page
        output = self.client.get(reverse('user-logout'))
        self.assertEqual(output.status_code, 200) # same exact problem
        self.assertTemplateUsed(output, 'user-logout.html')
        

class LeaderboardTestCase(TestCase):
    
    def setUp(self):
        # Create users
        self.user1 = get_user_model().objects.create_user(username='testuser1', password='TUpassword12')
        self.user2 = get_user_model().objects.create_user(username='testuser2', password='TUpassword23')

        # Create GameScore objects for the users
        GameScore.objects.create(user=self.user1, score=100)
        GameScore.objects.create(user=self.user2, score=150)
        
        # Ensure profiles exist for both users and avoid duplicates
        try:
            Profile.objects.get_or_create(user=self.user1, profile_image='/images/profile_pics/cat6.png')
            Profile.objects.get_or_create(user=self.user2, profile_image='/images/profile_pics/cat4.png')
        except IntegrityError:
           pass
  
    @patch('core.models.Profile.objects.get')
    def test_leaderboard_page(self, mock_get_profile):
        # Create mock data for profiles with fixed image paths
        mock_profile1 = Profile(user=self.user1, profile_image='/images/profile_pics/cat6.png')
        mock_profile2 = Profile(user=self.user2, profile_image='/images/profile_pics/cat4.png')

        # Mock the profile retrieval to return the fixed images
        mock_get_profile.side_effect = lambda user: mock_profile1 if user == self.user1 else mock_profile2
        
        # Simulate login for testuser1
        self.client.login(username='testuser1', password='TUpassword12')

        # Request the leaderboard page
        response = self.client.get(reverse('leaderboard'))  # Adjust URL name as per your setup

        # Check the profile images after mocking
        leaderboard_data = response.context['leaderboard_data']
        
        # Check the profile image paths
        self.assertEqual(leaderboard_data[0]['profile_image'], '/images/profile_pics/cat4.png')
        self.assertEqual(leaderboard_data[1]['profile_image'], '/images/profile_pics/cat6.png')

        # Check the leaderboard scores
        self.assertEqual(leaderboard_data[0]['total_score'], 150)  # `testuser2` has the higher score
        self.assertEqual(leaderboard_data[1]['total_score'], 100)  # `testuser1` has the lower score

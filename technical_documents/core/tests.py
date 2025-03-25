# Author: Surin Chai 

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from .forms import CreateUserForm, LoginForm, UserUpdateForm, UserDeleteForm
from django.core import mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from .models import Location
from core.models import Profile       
from minigames.models import GameScore  




# Test all in forms.py

class TestCreateUserForm(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }
        form = CreateUserForm(data=data)
        self.assertTrue(form.is_valid(), "The form should be valid with matching passwords and proper data.")

    def test_invalid_form_password_mismatch(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'differentpassword',
        }
        form = CreateUserForm(data=data)
        self.assertFalse(form.is_valid(), "The form should be invalid if the passwords do not match.")
        self.assertIn('password2', form.errors)

class TestLoginForm(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # Create a user to test login
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='complexpassword123')

    def test_login_form_valid(self):
        # AuthenticationForm (and our LoginForm) requires a request instance.
        request = self.factory.get('/')
        form = LoginForm(request=request, data={'username': 'testuser', 'password': 'complexpassword123'})
        self.assertTrue(form.is_valid(), "The login form should be valid with correct credentials.")

    def test_login_form_invalid(self):
        request = self.factory.get('/')
        form = LoginForm(request=request, data={'username': 'testuser', 'password': 'wrongpassword'})
        self.assertFalse(form.is_valid(), "The login form should be invalid with incorrect credentials.")

class TestUserUpdateForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='complexpassword123')

    def test_valid_update(self):
        data = {'username': 'updateduser', 'email': 'updated@example.com'}
        form = UserUpdateForm(data=data, instance=self.user)
        self.assertTrue(form.is_valid(), "UserUpdateForm should be valid with new, unique username and email.")
        updated_user = form.save()
        self.assertEqual(updated_user.username, 'updateduser')
        self.assertEqual(updated_user.email, 'updated@example.com')

    def test_invalid_update_duplicate_username(self):
        # Create another user with the username to duplicate
        User.objects.create_user(username='duplicate', email='dup@example.com', password='somepassword')
        data = {'username': 'duplicate', 'email': 'updated@example.com'}
        form = UserUpdateForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid(), "UserUpdateForm should be invalid if the username already exists.")
        self.assertIn('username', form.errors)

    def test_invalid_update_duplicate_email(self):
        # Create another user with the email to duplicate
        User.objects.create_user(username='unique', email='dup@example.com', password='somepassword')
        data = {'username': 'updateduser', 'email': 'dup@example.com'}
        form = UserUpdateForm(data=data, instance=self.user)
        self.assertFalse(form.is_valid(), "UserUpdateForm should be invalid if the email already exists.")
        self.assertIn('email', form.errors)

class TestUserDeleteForm(TestCase):
    def test_delete_form(self):
        user = User.objects.create_user(username='todelete', email='todelete@example.com', password='somepassword')
        # Bind the form with an empty dictionary (since there are no fields)
        form = UserDeleteForm(data={}, instance=user)
        self.assertTrue(form.is_valid(), "UserDeleteForm should be valid even if it has no fields.")

# Test all in views.py

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create an active user for login-related tests.
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="complexpassword123"
        )
        self.user.is_active = True
        self.user.save()

    def test_landing_page(self):
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")

    def test_register_get(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_register_post_valid(self):
        initial_user_count = User.objects.count()
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        }
        response = self.client.post(reverse("register"), data)
        # Should redirect to the "check your email" page after successful registration.
        self.assertRedirects(response, reverse("check-your-email"))
        self.assertEqual(User.objects.count(), initial_user_count + 1)
        new_user = User.objects.get(username="newuser")
        # New accounts are inactive until email confirmation.
        self.assertFalse(new_user.is_active)
        # Ensure an email was sent.
        self.assertEqual(len(mail.outbox), 1)

    def test_activate_valid(self):
        # Create an inactive user to activate.
        inactive_user = User.objects.create_user(
            username="inactive",
            email="inactive@example.com",
            password="complexpassword123"
        )
        inactive_user.is_active = False
        inactive_user.save()
        uid = urlsafe_base64_encode(force_bytes(inactive_user.pk))
        token = default_token_generator.make_token(inactive_user)
        url = reverse("activate", kwargs={"uidb64": uid, "token": token})
        response = self.client.get(url)
        # Expect a redirect to the activation success page.
        self.assertRedirects(response, reverse("activation-success"))
        inactive_user.refresh_from_db()
        self.assertTrue(inactive_user.is_active)

    def test_activate_invalid(self):
        # Use an invalid uid and token.
        uid = urlsafe_base64_encode(force_bytes(9999))
        token = "invalid-token"
        url = reverse("activate", kwargs={"uidb64": uid, "token": token})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Activation link is invalid")

    def test_activation_success(self):
        response = self.client.get(reverse("activation-success"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accountactivationsuccess.html")

    def test_check_your_email(self):
        response = self.client.get(reverse("check-your-email"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkyouremail.html")

    def test_my_login_get(self):
        response = self.client.get(reverse("my-login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-login.html")

    def test_my_login_post_valid(self):
        data = {'username': 'testuser', 'password': 'complexpassword123'}
        response = self.client.post(reverse("my-login"), data)
        # On successful login, should redirect to the dashboard.
        self.assertRedirects(response, reverse("dashboard"))

    def test_my_login_post_invalid(self):
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse("my-login"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-login.html")
        # Optionally, you can check for form errors in response.context

    def test_privacy_policy(self):
        response = self.client.get(reverse("privacy-policy"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "privacy_policy.html")

    def test_dashboard(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard.html")

    def test_how_to_play(self):
        response = self.client.get(reverse("how-to-play"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "how_to_play.html")

    def test_user_logout(self):
        # Log in the user.
        self.client.login(username="testuser", password="complexpassword123")
        response = self.client.get(reverse("user-logout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user-logout.html")
        # Verify the user is logged out.
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_user_profile_get(self):
        self.client.login(username="testuser", password="complexpassword123")
        response = self.client.get(reverse("user-profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user-profile.html")
        self.assertIn("u_form", response.context)

    def test_user_profile_post(self):
        self.client.login(username="testuser", password="complexpassword123")
        data = {'username': 'updateduser', 'email': 'updated@example.com'}
        response = self.client.post(reverse("user-profile"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user-profile.html")
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_deleteAccount_get(self):
        self.client.login(username="testuser", password="complexpassword123")
        response = self.client.get(reverse("delete-account"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete-account.html")
        self.assertIn("delete_form", response.context)

    def test_deleteAccount_post(self):
        # Create a new user to test account deletion.
        delete_user = User.objects.create_user(
            username="todelete",
            email="todelete@example.com",
            password="complexpassword123"
        )
        self.client.login(username="todelete", password="complexpassword123")
        response = self.client.post(reverse("delete-account"), {})
        self.assertRedirects(response, reverse("landing"))
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="todelete")



from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

# Imports for app testing
from .apps import UsersConfig

#Imports for models and views testing
from .models import Profile

# Create your tests here.
# Testing the app for the blog section
class TestUsersConfig(TestCase):

    def test_users_app(self):
        self.assertEqual("users", UsersConfig.name)
        self.assertEqual("users", apps.get_app_config("users").name)

#Testing a model for the users
class TestUsersModels(TestCase):

    def test_create_post(self):
        User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='passwordtest')
        self.client.login(username='testuser', password='passwordtest')
        profile = Profile(firstname='Firstname', lastname='Lastname', profile_intro='Profile intro test', image='/user_images/image.jpg')
        profile.save()
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.firstname, 'Firstname')
        self.assertEqual(profile.lastname, 'Lastname')
        self.assertEqual(profile.profile_intro, 'Profile intro test')
        self.assertEqual(profile.image, '/user_images/image.jpg')
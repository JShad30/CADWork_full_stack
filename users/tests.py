from django.test import TestCase
from django.apps import apps

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
        profile = Profile(username='username', firstname='Firstname', lastname='Lastname', profile_intro='Profile intro test', image='image.jpg')
        profile.save()
        self.assertEqual(profile.user, 'username')
        self.assertEqual(profile.firstname, 'Firstname')
        self.assertEqual(profile.lastname, 'Lastname')
        self.assertEqual(profile.profile_intro, 'Profile intro test')
        self.assertEqual(profile.image, 'image.jpg')
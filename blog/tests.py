from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

#Imports for app testing
from .apps import BlogConfig

#Imports for views testing
from .models import Post, PostComment

# Create your tests here.
# Testing the app for the blog section
class TestBlogConfig(TestCase):

    def test_blog_app(self):
        self.assertEqual("blog", BlogConfig.name)
        self.assertEqual("blog", apps.get_app_config("blog").name)
        
#Testing the views
class TestBlogViews(TestCase):
    def test_get_home_blog_page(self):
        blog_home = self.client.get("/blog/")
        self.assertEqual(blog_home.status_code, 200)
        self.assertTemplateUsed(blog_home, "blog/home.html")
from django.test import TestCase
from django.apps import apps

#Imports for app testing
from .apps import BlogConfig

#Imports for model and views testing
from .models import Post, PostComment

# Create your tests here.
# Testing the app for the blog section
class TestBlogConfig(TestCase):

    def test_events_app(self):
        self.assertEqual("blog", BlogConfig.name)
        self.assertEqual("blog", apps.get_app_config("blog").name)

#Testing a model for the blog
class TestBlogModels(TestCase):

    def test_create_post(self):
        post = Post(title='Blog post', intro='Basic blog post content intro', content='Content to go into the textfield', image='image.jpg')
        post.save()
        self.assertFalse(post.title, 'Blog post')
        self.assertEqual(post.intro, 'Basic blog post content intro')
        self.assertEqual(post.content, 'Content to go into the textfield')
        self.assertEqual(post.image, 'image.jpg')

    def test_create_comment(self):
        post_comment = PostComment(comment='Test comment')
        self.assertEqual(post_comment.comment, 'Test comment')

#Testing the views
class TestBlogViews(TestCase):

    def test_get_home_blog_page(self):
        blog_home = self.client.get("/blog/")
        self.assertEqual(blog_home.status_code, 200)
        self.assertTemplateUsed(blog_home, "blog/home.html")
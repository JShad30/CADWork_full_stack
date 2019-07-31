from django.db import models
"""timezone is a built in django library that allows you to bring in the time something was created"""
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
	title = models.CharField(max_length=100)
	intro = models.CharField(max_length=250)
	content = models.TextField()
	image = models.ImageField(default='blog_default.jpg', upload_to='blog_images')

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 600 or img.width > 1200:
			output_size = (600,1200)
			img.header(output_size)
			img.save(self.image.path)

	"""Ensure the timezone.now doesn't have parenthesis(). That would run the function at that moment"""
	date_posted = models.DateTimeField(default=timezone.now)
	"""CASCADE - tells django that if a user is deleted all their posts will be deleted too"""
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})




	



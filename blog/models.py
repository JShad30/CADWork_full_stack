from django.db import models
"""timezone is a built in django library that allows you to bring in the time something was created"""
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	"""Ensure the timezone.now doesn't have parenthesis(). That would run the function at that moment"""
	date_posted = models.DateTimeField(default=timezone.now)
	"""CASCADE - tells django that if a user is deleted all their posts will be deleted too"""
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})



from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(default='blog_default.jpg', upload_to='blog_images')

	def save(self):
		super().save()

		image = Image.open(self.image.path)

		if image.height > 600 or image.width > 1200:
			output_size = (600,1200)
			image.header(output_size)
			image.save(self.image.path)

	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})




	



from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(default='blog-default.jpg', upload_to='blog_images')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        blog_image = Image.open(self.image.path)

        if blog_image.height > 1200 or blog_image.width > 700:
            blog_output_size = (1200, 700)
            blog_image.thumbnail(blog_output_size)
            blog_image.save(self.image.path)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
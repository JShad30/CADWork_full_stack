from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

"""Creating a model for the blog posts. Uses appropriate standard field types from within Python."""
class Post(models.Model):
	title = models.CharField(max_length=100)
	intro = models.CharField(max_length=250)
	content = models.TextField()
	#The image is saved to 'blog_images' within the static file. Is the user does not upload an image, their post will display the 'blog-default.jpg' image
	image = models.ImageField(default='blog-default.jpg', upload_to='blog_images')
	date_posted = models.DateTimeField(default=timezone.now)
	#Foreign key links the user to their blog posts
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	#The following save function resizes the images saved by the user to ensure the images do not take up more space than is needed
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		blog_image = Image.open(self.image.path)

		#Check to see whether the image is larger than the standard size, if so, resize
		if blog_image.height != 700 or blog_image.width != 1200:
			output_size = (1200, 700)
			blog_image.thumbnail(output_size)
			blog_image.save(self.image.path)

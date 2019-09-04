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
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	#The following save function resizes the images saved by the user to ensure the images do not take up more space than is needed
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		image = Image.open(self.image.name)

		#Check to see whether the image is larger than the standard size, if so, resize
		if image.height != 700 or image.width != 1200:
			output_size = (1200, 700)
			image.thumbnail(output_size)
			image.save(self.image.name)

	class Meta:
		ordering = ['-date_posted']


#Model to allow a user to comment on a blog post.
class PostComment(models.Model):
	comment = models.TextField()	
	comment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='blog_comments')
	author = models.ForeignKey(User, null=False, default=1, on_delete=models.CASCADE, related_name='blog_comments')

	def __str__(self):
		return self.comment

	class Meta:
		ordering = ['-comment_date']

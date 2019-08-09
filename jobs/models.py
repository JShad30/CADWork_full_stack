from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Job(models.Model):
	job_name = models.CharField(max_length=100, default='Default Project Name')
	job_overview = models.CharField(max_length=250, default='Default Project Overview')
	job_description = models.TextField()
	job_location_town = models.CharField(max_length=30)
	job_location_county = models.CharField(max_length=25)
	job_image = models.ImageField(default='job-default.jpg', upload_to='job_images')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.job_name

	def get_absolute_url(self):
		return reverse('job-detail', kwargs={'pk': self.pk})

		def save(self, *args, **kwargs):
			super().save(*args, **kwargs)

			job_image = Image.open(self.image.path)

			if job_image.width > 1200 or job_image.height > 700:
				output_size = (1200, 700)
				job_image.resize(output_size)
				job_image.save(self.image.path)

			job_image.close()



class JobBid(models.Model):
	job_bid_amount = models.DecimalField(max_digits=7, decimal_places=2)
	job_name = models.ForeignKey(Job, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.job_name

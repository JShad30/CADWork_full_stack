from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


"""Creating the classes for the jobs"""
#The job model will take information when the user fills in the form.
class Job(models.Model):
	job_name = models.CharField(max_length=100, default='Default Project Name')
	job_overview = models.CharField(max_length=250, default='Default Project Overview')
	job_description = models.TextField()
	job_location_town = models.CharField(max_length=30)
	job_location_county = models.CharField(max_length=25)
	#If the user does not save an image, 'job-default.jpg' will be used
	image = models.ImageField(default='job-default.jpg', upload_to='job_images')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, related_name='jobs', null=False, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.job_name
	
	def get_absolute_url(self):
		return reverse('job-detail', kwargs={'pk': self.pk})

	#Save function to resize the image to save space.
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		job_image = Image.open(self.image.path)

		if job_image.width != 1200 or job_image.height != 700:
			output_size = (1200, 700)
			job_image.resize(output_size)
			job_image.save(self.image.path)



#Job bid model to be used when a user fills in a bid on the job form
class JobBid(models.Model):
	job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='bids')
	author = models.ForeignKey(User, related_name='bids', null=False, default=1, on_delete=models.CASCADE)
	job_bid_amount = models.DecimalField(max_digits=7, decimal_places=2, default=1)

	def __int__(self):
		return self.job_bid_amount

	def get_absolute_url(self):
		return reverse('jobs-home')

		def save(self, *args, **kwargs):
			super().save(*args, **kwargs)



#Form to handle the upload of files on the Active Job pages
class JobFileUpload(models.Model):
	file_name = models.CharField(max_length=100)
	uploaded_file = models.FileField(upload_to='job_files')
	author = models.ForeignKey(User, max_length=100, related_name='files', null=False, default=1, on_delete=models.CASCADE)
	job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='files')

	def __str__(self):
		return self.file_name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default='First Name')
    lastname = models.CharField(max_length=30, default='Last Name')
    profile_intro = models.TextField(default='Default intro. Change this to tell other users a little more about yourself')
    image = models.ImageField(default='user-default.jpg', upload_to='user_images')
    member_since = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        profile_image = Image.open(self.image.path)

        if profile_image.height > 250 or profile_image.width > 250:
            output_size = (250, 250)
            profile_image.thumbnail(output_size)
            profile_image.save(self.image.path)


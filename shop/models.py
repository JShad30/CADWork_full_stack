from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=250, default="")
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='product_images')
    
    def __str__(self):
        return f'{self.product_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        product_image = Image.open(self.image.path)

        if product_image.height > 500 or product_image.width > 500:
            output_size = (500, 500)
            product_image.thumbnail(output_size)
            product_image.save(self.image.path)
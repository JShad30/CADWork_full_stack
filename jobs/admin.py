from django.contrib import admin
from .models import Job, JobFileUpload#JobBid, 

# Register your models here.
admin.site.register(Job)
#admin.site.register(JobBid)
admin.site.register(JobFileUpload)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import JobBid, JobFileUpload

#Create a bid for a job
class JobBidForm(forms.ModelForm):
    bid = forms.DecimalField()
    
    class Meta:
        model = JobBid
        fields = ['job_bid_amount']


class JobFileUploadForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = JobFileUpload
        fields = ['file_name', 'uploaded_file']
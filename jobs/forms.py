from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import JobBid

#Create a bid for a job
class JobBidForm(forms.ModelForm):
    bid = forms.DecimalField()
    
    class Meta:
        model = JobBid
        fields = ['job_bid_amount']
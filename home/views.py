from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def terms(request):
    return render(request, 'home/terms.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form', message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=FALSE)
    return render(request, 'home/contact.html')
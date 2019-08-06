from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from blog.models import Post

# Create your views here.
def home(request):
    blog_context = {
		'posts': Post.objects.all()
	}
    return render(request, 'home/index.html', blog_context)



class HomePostView(ListView):
	model = Post
	template_name = 'home/index.html'
	context_object_name = 'posts'
	order = ['-date_posted']
	paginate_by = 3



def about(request):
    return render(request, 'home/about.html')



def terms(request):
    return render(request, 'home/terms.html')



def privacy(request):
    return render(request, 'home/privacy.html')



def contact(request):
    if request.method == 'POST':
        contact_email = request.POST['email']
        message = request.POST['message']

        send_mail('CADWork message from ' + contact_email, 
            message, 
            settings.EMAIL_HOST_USER, 
            [settings.EMAIL_HOST_USER], 
            fail_silently=False
        )
        return redirect('message_received')
    return render(request, 'home/contact.html')



def message_received(request):
    return render(request, 'home/message_received.html')
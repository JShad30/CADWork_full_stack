from django.shortcuts import render

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
    return render(request, 'home/contact.html')
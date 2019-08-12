from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

"""The shop home page will display all products available for purchase"""
def home(request):
    context = {
        'shop': Product.objects.all()
    }
    return render(request, 'shop/home.html', context)

class ProductListView(ListView):
	model = Product
	template_name = 'shop/home.html'
	context_object_name = 'shop'
	order = ['-date_posted']
	paginate_by = 9
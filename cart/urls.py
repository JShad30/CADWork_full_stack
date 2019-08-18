from django.urls import path
from .views import home, add_to_cart, adjust_cart

"""Urls for the cart section of the site. These urls will be added to the '/cart' extension set up within the main site urls file in the 'cadwork' folder"""
urlpatterns = [
    path('', home, name='cart-home'),
    path('add/<int:id>/', add_to_cart, name='add_to_cart'),
    path('adjust/<int:id>/', adjust_cart, name='adjust_cart')
]
from django.urls import path
from .views import home, add_to_cart, adjust_cart

urlpatterns = [
    path('', home, name='cart-home'),
    path('add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    path('adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]
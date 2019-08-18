from django.urls import path
from .views import home

"""Urls for the checkout section of the site. These urls will be added to the '/checkout' extension set up within the main site urls file in the 'cadwork' folder"""
urlpatterns = [
    path('', home, name='checkout-home')
]

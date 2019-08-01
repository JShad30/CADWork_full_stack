from django.urls import path
from .views import home, about, terms, privacy, contact

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name='contact'),
]
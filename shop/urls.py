from django.urls import path
from .views import ProductListView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='shop-home'),
]
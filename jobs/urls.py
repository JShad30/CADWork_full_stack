from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView
from . import views

urlpatterns = [
    path('', JobListView.as_view(), name='jobs-home'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
]
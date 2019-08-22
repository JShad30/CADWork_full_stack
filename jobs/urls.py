from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView, job_active_view, job_bid_view
from . import views

"""Urls for the jobs section of the site. These urls will be added to the '/jobs' extension set up within the main site urls file in the 'cadwork' folder"""
#<int:pk> extension to specify the url extension depending on the specific post or user who created the post.
urlpatterns = [
    path('', JobListView.as_view(), name='jobs-home'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/bid/', views.job_bid_view, name='job-bid'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('job/<int:pk>/active/', views.job_active_view, name='job-active'),
]
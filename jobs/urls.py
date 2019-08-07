from django.urls import path
from .views import JobListView, JobConfirmBid, JobDetailView, JobCreateView
from . import views

urlpatterns = [
    path('', JobListView.as_view(), name='jobs-home'),
    path('user/<str:username>', JobConfirmBid.as_view(), name='user-jobs'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='jobs-detail'),
    path('job/new/', JobCreateView.as_view(), name='jobs-create'),
]
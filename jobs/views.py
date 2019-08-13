from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job, JobBid

def home(request):
	context = {'jobs': Job.objects.all()}
	return render(request, 'jobs/home.html', context)


class JobListView(ListView):
	model = Job
	template_name = 'jobs/home.html'
	context_object_name = 'jobs'
	order = ['-date_posted']
	paginate_by = 9


class JobDetailView(DetailView):
	model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
	model = Job
	fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Job
	fields = ['job_name', 'image']
		
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
	"""Stop the user from being able to access another users post"""
	def test_func(self):
		job = self.get_object()
		if self.request.user == job.author:
			return True
		else:
			return False
		
		
class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Job
	success_url = '/profile'
		
	def test_func(self):
		job = self.get_object()
		if self.request.user == job.author:
			return True
		else:
			return False


class JobBidView(LoginRequiredMixin, CreateView):
	model = JobBid
	fields = ['job_bid_amount']
	template_name = 'jobs/job_confirm_bid.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class JobBidDisplay(LoginRequiredMixin, ListView):
	model = JobBid
	context = {'bids': JobBid.objects.all()}

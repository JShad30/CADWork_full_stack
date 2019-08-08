from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Job

def home(request):
	context = {
		'jobs': Job.objects.all()
	}
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
	fields = ['job_name', 'job_description', 'job_address_line_one', 'job_address_town', 'job_address_county', 'job_address_postcode', 'job_image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
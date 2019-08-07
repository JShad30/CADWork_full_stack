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
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	order = ['-date_posted']
	paginate_by = 9


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Job
	success_url = '/profile'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class JobDetailView(DetailView):
	model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
	model = Job
	fields = ['title', 'intro', 'content', 'blog_image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
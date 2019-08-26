from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job, JobBid, JobFileUpload
from .forms import JobBidForm, JobFileUploadForm
from django.http import HttpResponseForbidden, HttpResponse
from django.urls import reverse
from django.core.files.storage import FileSystemStorage



"""Rendering the views for the jobs pages. As with the blogs section most will be created with classes"""
#Rendering the jobs home page. Takes context as an argument and displays all the blogs.
def home(request):
	context = {
		'jobs': Job.objects.all()
	}
	return render(request, 'jobs/home.html', context)



#List of jobs using standard ListView imported
class JobListView(ListView):
	model = Job
	template_name = 'jobs/home.html'
	context_object_name = 'jobs'
	order = ['-date_posted']
	paginate_by = 9



#Render the job details page
class JobDetailView(DetailView):
	model = Job

	#Get the context data to be able to display other blogs from within the detail view for the aside in 'post_detail.html'.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['job.files'] = JobFileUpload.objects.all()
		return context



#Enable users to be able to upload files to a job
class FileUploadView(CreateView):
	odel = JobFileUpload
	form_class = JobFileUploadForm
	success_url = reverse_lazy('job-detail')
	template_name = 'jobs/job_upload.html'

#Function view to show the bids and assign a bid to that job
#def job_upload_view(request, pk):
    #if not request.user.is_authenticated:
        #return redirect('login')
    #else:
        #try:
            #if (request.user.is_authenticated):
                #files = JobFileUpload.objects.all()
                #job = get_object_or_404(Job, pk=pk)
                #if request.method == "POST":
                   #form = JobFileUploadForm(request.POST)
                    #if form.is_valid():
                        #file = form.save(commit=False)
                        #file.author = request.user
                        #file.job = job
                        #file.save()
                        #return redirect('job-detail', pk=job.pk)
                #else:
                    #form = JobFileUploadForm()

        #except User.DoesNotExist:
            #return HttpResponseForbidden()

    #return render(request, 'jobs/job_upload.html', {'form': form, 'files': files, 'job': job})



#Rendering the job create form. Fields uses the fields created in the 'models.py' file
class JobCreateView(LoginRequiredMixin, CreateView):
	model = Job
	fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Function view to show the bids and assign a bid to that job
def job_bid_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_authenticated):
                bids = JobBid.objects.all()
                job = get_object_or_404(Job, pk=pk)
                if request.method == "POST":
                    form = JobBidForm(request.POST)
                    if form.is_valid():
                        bid = form.save(commit=False)
                        bid.author = request.user
                        bid.job = job
                        bid.save()
                        return redirect('job-detail', pk=job.pk)
                else:
                    form = JobBidForm()

        except User.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'jobs/job_confirm_bid.html', {'form': form, 'bids': bids, 'job': job})



#Job update form is the same as the create form. Existing information wil be already included in the form
class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Job
	#Only the name and image can be changed as it would be unfair for the user to be able to update the job, while they were already taking bids from other users.
	fields = ['job_name', 'image']
		
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
	#Stop the user from being able to access another users post
	def test_func(self):
		job = self.get_object()
		if self.request.user == job.author:
			return True
		else:
			return False
		


#Handle the logic to enable the user to be able to delete a blog
class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Job
	success_url = '/profile'
	fields = ['job_name']
	
	#Stop a user from being able to access another users post
	def test_func(self):
		job = self.get_object()
		if self.request.user == job.author:
			return True
		else:
			return False



#class JobBidAcceptView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	#model = JobBidAccept
	#success_url = '/profile'
	#fields = ['job_name']

	#Stop a user from being able to access another users post
	#def test_func(self):
		#job = self.get_object()
		#if self.request.user == job.author:
			#return True
		#else:
			#return False

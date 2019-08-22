from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job, JobBid
from .forms import BidForm
from django.http import HttpResponseForbidden, HttpResponse
from django.urls import reverse

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
		context['job.bids'] = JobBid.objects.all()
		return context



# Logic to allow the page to show all of the bids made on a job
#class JobBidDisplay(LoginRequiredMixin, ListView):
	#model = JobBid
	#context_object_name = 'bids'

	#def get_queryset(self):
		#bids = get_object_or_404(JobBid, job=self.kwargs.get('job'))
		#return JobBid.objects.filter(job=id).order_by('-job_bid_amount')



#def job_bid_view(request, pk):
    #if not request.user.is_authenticated:
        #return redirect('login')
    #else:
        #try:
            #if (request.user.is_superuser or request.user):
                #bid = JobBid.objects.all()
                #job = get_object_or_404(Job, pk=pk)
                #if request.method == "POST":
                    #form = BidForm(request.POST)
                    #if form.is_valid():
                        #bid = form.save(commit=False)
                        #bid.author = request.user
                        #bid.post = bid
                        #bid.save()
                        #return redirect('jobs-home')
                #else:
                    #form = BidForm()

        #except User.DoesNotExist:
            #return HttpResponseForbidden()

    #return render(request, 'jobs/job_confirm_bid.html', {'form': form})




#class JobBidDisplay(LoginRequiredMixin, ListView):
	#model = JobBid
	#context = {'bids': JobBid.objects.filter(id).order_by('-job_bid_amount')}



#Rendering the job create form. Fields uses the fields created in the 'models.py' file
class JobCreateView(LoginRequiredMixin, CreateView):
	model = Job
	fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Rendering the bid form, allowing the user to type a bid amount and assigning it to the specific job
class BidCreateView(LoginRequiredMixin, CreateView):
	model = JobBid
	fields = ['job', 'job_bid_amount']
	template_name = 'jobs/job_confirm_bid.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



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
	
	#Stop the user from being able to access another users post
	def test_func(self):
		job = self.get_object()
		if self.request.user == job.author:
			return True
		else:
			return False



#Rendering the page where the user is able to bid on a job
#class JobBidView(LoginRequiredMixin, CreateView):
	#model = JobBid
	#Use the fields from the JobBid class created in 'models.py' file
	#fields = ['job_bid_amount']
	#template_name = 'jobs/job_confirm_bid.html'

	#def form_valid(self, form):
		#form.instance.author = self.request.user
		#return super().form_valid(form)
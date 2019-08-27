from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job, JobFileUpload#JobBid, 
from .forms import JobFileUploadForm#JobBidForm, 
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

	#Get the context data to be able to display other blogs from within the detail view for the uploaded files in 'job_detail.html'.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['uploaded_files'] = JobFileUpload.objects.all()
		return context



#Function view to show the bids and assign a bid to that job
@login_required
def job_upload_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_authenticated):
                uploaded_files = JobFileUpload.objects.all()
                job = get_object_or_404(Job, pk=pk)
                if request.method == "POST":
                    form = JobFileUploadForm(request.POST, request.FILES)
                    if form.is_valid():
                        uploaded_file = form.save(commit=False)
                        uploaded_file.author = request.user
                        uploaded_file.job = job
                        uploaded_file.save()
                        return redirect('job-detail', pk=job.pk)
                else:
                    form = JobFileUploadForm()

        except User.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'jobs/job_upload.html', {'form': form, 'uploaded_files': uploaded_files, 'job': job})



#Rendering the job create form. Fields uses the fields created in the 'models.py' file
class JobCreateView(LoginRequiredMixin, CreateView):
	model = Job
	fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Function view to show the bids and assign a bid to that job
#def job_bid_view(request, pk):
    #if not request.user.is_authenticated:
        #return redirect('login')
    #else:
        #try:
            #if (request.user.is_authenticated):
                #bids = JobBid.objects.all()
                #job = get_object_or_404(Job, pk=pk)
                #if request.method == "POST":
                    #form = JobBidForm(request.POST)
                    #if form.is_valid():
                        #bid = form.save(commit=False)
                        #bid.author = request.user
                        #bid.job = job
                        #bid.save()
                        #return redirect('job-detail', pk=job.pk)
                #else:
                    #form = JobBidForm()

        #except User.DoesNotExist:
            #return HttpResponseForbidden()

    #return render(request, 'jobs/job_confirm_bid.html', {'form': form, 'bids': bids, 'job': job})



#Job update form is the same as the create form. Existing information will be already included in the form
class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Job
	fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']
		
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


#View for the uploaded files checkout in jobs"""
@login_required
def job_checkout(request):
    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        p_form = MakePaymentForm(request.POST)

        #Check that both forms are valid
        if o_form.is_valid() and p_form.is_valid():
            order = o_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            uploaded_files = request.session.get('jobs', {})
            total = uploaded_file.file_price

            for id, quantity in uploaded_files.items():
                uploade = get_object_or_404(JobFileUpload, pk=id)
                total += quantity * product.product_price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = 1
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = 'GBP',
                    description = request.user.email,
                    card = p_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card has been declined')

            #If statement to determine which message to print
            if customer.paid:
                messages.error(request, 'Your payment has been successfully processed')
                request.session['cart'] = {}
                return redirect('profile')
            else:
                messages.error(request, 'We were unable to accept your payment')

        #Message to print of forms are not valid
        else:
            print(p_form.errors)
            messages.error(request, 'We were unable to accept a payment with the credit or debit card you provided.')
    
    else:
        p_form = MakePaymentForm()
        o_form = OrderForm()

    return render(request, 'checkout/job-checkout.html', {'o_form': o_form, 'p_form': p_form, 'publishable': settings.STRIPE_PUBLISHABLE})
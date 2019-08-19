from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

"""Function view for the home page of the blog. The context """
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	# Rendering the blog home page and taking the context as an argument that displays all the posts.
	return render(request, 'blog/home.html', context)



"""Using class based views for the rest of the blog pages"""
#List the posts
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	order = ['-date_posted']
	paginate_by = 6



#Same as the views on the home page but specifically for the user who created the blog 
class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 6

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')



#Individual post view
class PostDetailView(DetailView):
	model = Post

	#Get the context data to be able to display other blogs from within the detail view for the aside in 'post_detail.html'.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Post.objects.all()[:3]
		return context
		


#Post create class to be used in the form within the 'post_form.html'.
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	#Fields taken from the model created in 'models.py' file 
	fields = ['title', 'intro', 'content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Same as the post create view above. As this view is an update view it will start with information in the create form. The 'LoginRequiredMixin' and 'UserPassesTestMixin' ensures only the user who created the post can access this page.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	#Fields same as the PostCreateView
	fields = ['title', 'intro', 'content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#Stop the user from being able to access another users post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False



#View to enable the user who created the post to be able to delete it.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/blog'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False
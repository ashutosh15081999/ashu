from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blogdesign/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blogdesign/home.html'
	context_object_name = 'post'
	ordering = ['-date']

#<app>/<model>_<viewtype.html>

class PostDetailView(DetailView):
	model = Post
	template_name = 'blogdesign/post.html'
	context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	template_name = 'blogdesign/post_form.html'
	fields = [
		'title',
		'content',
	]

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	template_name = 'blogdesign/post_form.html'
	fields = [
		'title',
		'content',
	]

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	template_name = 'blogdesign/delete_post.html'
	success_url = '/blog/home/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
    return render(request, 'blogdesign/about.html', {'title': 'About'})


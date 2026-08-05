from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm
from django .urls import reverse_lazy

# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'postlist.html'
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    template_name = 'postcreate.html'
    fields = '__all__'
    context_object_name = 'posts'


class UpdatePost(UpdateView):
    model = Post
    template_name = 'postcreate.html'
    fields = ['title','description','image']


class DeletePost(DeleteView):
    model = Post
    template_name = 'postdelete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('list')
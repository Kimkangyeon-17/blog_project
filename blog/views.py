from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update_form.html'
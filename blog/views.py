from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

class HomeView(TemplateView):
    template_name = 'blog/home.html'

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_posts = Post.objects.order_by('-hit')[:3]
    return render(
        request,
        'home_page/landing.html',
        {
            'recent_posts' : recent_posts,
        }
    )
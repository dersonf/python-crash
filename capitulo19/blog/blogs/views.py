from django.shortcuts import render

from .models import BlogPost


def index(request):
    """The home page of Blogs."""
    return render(request, 'blogs/index.html')


def posts(request):
    """Return the main posts page."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


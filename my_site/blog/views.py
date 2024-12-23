from django.shortcuts import render, get_object_or_404
from datetime import date

from.models import Post

# Create your views here.

def starting_page(req):
    latest_posts = Post.objects.all().order_by('-created_date')[:3]
    return render(req, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(req):
    all_posts = Post.objects.all().order_by('-created_date')
    return render(req, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(req, slug):
    try:
        identified_post = get_object_or_404(Post, slug = slug)
    except:
        return
    return render(req, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()
    })
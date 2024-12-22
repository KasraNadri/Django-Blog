from django.shortcuts import render
from datetime import date

from.models import Post

# Create your views here.


all_posts = [
     
]

def get_date(all_posts):
    return all_posts

def starting_page(req):
    latest_posts = Post.objects.all().order_by('-created_date')[:3]
    return render(req, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(req):
    return render(req, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(req, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(req, 'blog/post-detail.html', {
        'post': identified_post
    })
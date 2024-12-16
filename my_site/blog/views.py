from django.shortcuts import render

# Create your views here.


def starting_page(req):
    return render(req, 'blog/index.html')

def posts(req):
    return render(req, 'blog/all-posts.html')

def post_detail(req):
    pass
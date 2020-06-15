from django.shortcuts import render, get_object_or_404
from .models import *
def posts(request):
    page_title = 'Все новости'
    page_description = 'page_description'
    allposts = Post.objects.filter(is_active=True)
    return render(request, 'pages/posts.html', locals())
def post(request,slug):
    post = get_object_or_404(Post,name_slug=slug)
    page_title = post.name
    page_description = ''
    return render(request, 'pages/post.html', locals())
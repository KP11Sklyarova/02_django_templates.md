from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *
# Create your views here.
def post_list(request):  
    posts = Post.objects.all()  
    return render(request, 'posts/list.html', {'posts': posts, 'title':"hello"})  
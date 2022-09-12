from django.shortcuts import render

# Create your views here.
from .models import posts


def all_posts(request):
    posts=Post.objects.all()
    return render(request,'posts.html',{'saror':posts})

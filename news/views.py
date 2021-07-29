from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'news': posts
    }
    return render(request, 'news/home.html', context)


def video(request):
    return render(request, 'news/video.html')


def blog(request):
    return render(request, 'news/blog.html')
# Create your views here.

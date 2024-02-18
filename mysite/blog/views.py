from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def my_blog(request):
    return HttpResponse("Hello from my blog")


def my_blog1(request):
    return HttpResponse("Hello from my article 1 in blog")


def my_blog2(request):
    return HttpResponse("Hello from my article 2 in blog")


def tab1(request):
    my_post = Post.objects.get(id=1)
    return render(request, "first_post.html", {"my_post": my_post})


def tab2(request):
    my_post = Post.objects.get(id=2)
    return render(request, "second_post.html", {"my_post_2": my_post})

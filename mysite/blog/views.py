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
    return render(request, "first_post", {})


def tab2(request):
    return render(request, "second_post", {})

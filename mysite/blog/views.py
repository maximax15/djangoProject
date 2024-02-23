from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import MyForm, PostForm


def my_blog(request):
    return HttpResponse("Hello from my blog")


def my_blog1(request):
    return HttpResponse("Hello from my article 1 in blog")


def my_blog2(request):
    return HttpResponse("Hello from my article 2 in blog")


def new_article(request):
    if request.method == "POST":
        new_post = PostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
    new_post_form = PostForm()
    return render(request, "new_article.html", {"new_post_form": new_post_form})


def base(request):
    return render(request, "base.html")


def tab1(request):
    my_post_1 = Post.objects.get(id=1)
    return render(request, "first_post.html", {"my_post_1": my_post_1})


def tab2(request):
    my_post_2 = Post.objects.get(id=2)
    return render(request, "second_post.html", {"my_post_2": my_post_2})


def tab3(request):
    my_post_3 = Post.objects.get(id=3)
    return render(request, "third_post.html", {"my_post_3": my_post_3})

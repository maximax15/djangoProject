from django.shortcuts import render, get_object_or_404, redirect
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


def update_article(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    if request.method == "POST":
        new_post = PostForm(request.POST, instance=post_obj)
        if new_post.is_valid():
            new_post.save()
            return redirect('/blog/list_post')
    post_form = PostForm(instance=post_obj)
    return render(request, "update_article.html", {"post_form": post_form, 'post_id': post_id})


def base(request):
    return render(request, "base.html")


def list_post(request):
    all = Post.objects.all()
    return render(request, "list_post.html", {"all": all})


def read_post(request, post_id):
    my_post = Post.objects.get(id=post_id)
    return render(request, "read_post.html", {"my_post": my_post})


def delete_article(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/blog/list_post')
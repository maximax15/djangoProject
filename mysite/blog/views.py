from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import MyForm, PostForm, LoginUser
from django.contrib.auth import authenticate, login, logout
from .models import Post
from rest_framework import generics
from .serializers import PostSerializers
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Home page")


def login_page(request):
    log = LoginUser()
    if request.method == "POST":
        log = LoginUser(request, data=request.POST)
        if log.is_valid():
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )

            if user is not None:
                login(request, user)
                return redirect("/blog/base")
    return render(request, "login.html", {"login": log})


def logout_page(request):
    logout(request)

    return redirect("/blog/login")

@login_required(login_url="/blog/login")
def new_article(request):
    if request.method == "POST":
        new_post = PostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
    new_post_form = PostForm()
    return render(request, "new_article.html", {"new_post_form": new_post_form})

@login_required(login_url="/blog/login")
def update_article(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    if request.method == "POST":
        new_post = PostForm(request.POST, instance=post_obj)
        if new_post.is_valid():
            new_post.save()
            return redirect("/blog/list_post")
    post_form = PostForm(instance=post_obj)
    return render(
        request, "update_article.html", {"post_form": post_form, "post_id": post_id}
    )


def base(request):
    return render(request, "base.html")

@login_required(login_url="/blog/login")
def list_post(request):
    all = Post.objects.all()
    return render(request, "list_post.html", {"all": all})


def read_post(request, post_id):
    my_post = Post.objects.get(id=post_id)
    return render(request, "read_post.html", {"my_post": my_post})

@login_required(login_url="/blog/login")
def delete_article(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("/blog/list_post")


class LoginView(TemplateView):
    def get(request):
        pass

    def post(request):
        pass

    def delete(request):
        pass


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = "pk"
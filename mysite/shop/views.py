from django.shortcuts import render
from django.http import HttpResponse


def my_shop(request):
    return HttpResponse("Hello from my shop")


def my_shop1(request):
    return HttpResponse("hello from article1 in shop")


def my_shop2(request):
    return HttpResponse("Hello from article2 in shop")

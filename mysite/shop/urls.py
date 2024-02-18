from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_shop),
    path("article1", views.my_shop1),
    path("article2", views.my_shop2),
]

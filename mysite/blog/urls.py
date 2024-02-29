from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_blog),
    path("article1", views.my_blog1),
    path("article2", views.my_blog2),
    path("base", views.base),
    path("new_article", views.new_article),
    path("list_post", views.list_post),
    path("read_post/<int:post_id>", views.read_post, name="read_post"),
    path("update_article/<int:post_id>", views.update_article, name='up_article'),
    path("delete_article/<int:post_id>", views.delete_article, name='del_article'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_page),
    path("logout", views.logout_page),
    path("logout", views.logout),
    path("base", views.base),
    path("new_article", views.new_article),
    path("list_post", views.list_post),
    path("read_post/<int:post_id>", views.read_post, name="read_post"),
    path("update_article/<int:post_id>", views.update_article, name='up_article'),
    path("delete_article/<int:post_id>", views.delete_article, name='del_article'),
    path("posts", views.PostListCreate.as_view(), name = "post-view-create"),
    path(
        "posts/<int:pk>",views.PostRetrieveUpdateDestroy.as_view(),name = "update"),
]

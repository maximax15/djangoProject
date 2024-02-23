from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_blog),
    path("article1", views.my_blog1),
    path("article2", views.my_blog2),
    path('tab1', views.tab1),
    path('tab2', views.tab2),
    path('tab3', views.tab3),
    path('new_article', views.new_article),
    path('base', views.base),
]

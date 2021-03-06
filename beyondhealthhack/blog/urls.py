from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r"<int:id>", views.blog, name='blog post'),
    path("post_blog", views.post_blog, name="post blog"),
]
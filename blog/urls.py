from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.get_blog, name="blog"),
    path("blog/<int:blog_id>/", views.blog_view, name="blog_view"),
]

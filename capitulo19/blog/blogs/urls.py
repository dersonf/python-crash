"""Defines URL patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # The posts page
    path('posts/', views.posts, name='posts'),
]
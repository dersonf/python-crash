"""Defines URL patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # The posts page
    path('posts/', views.posts, name='posts'),
    # The new post page
    path('new_post/', views.new_post, name='new_post'),
    # The edit post page.
    path('edit_post/<int:entry_id>', views.edit_post, name='edit_post'),
]
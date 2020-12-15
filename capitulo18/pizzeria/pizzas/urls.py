"""Defines URL patterns for pizzas."""

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizza toppings
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page about a pizza toppings
    path('topping/<int:topping_id>', views.topping, name='topping'),
]

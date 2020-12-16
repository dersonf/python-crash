from django.shortcuts import render
from .models import Pizza, Topping


def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Show all pizzas flavors."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def topping(request, topping_id):
    """Show details about a topping."""
    topping = Topping.objects.get(id=topping_id)
    pizza = Pizza.objects.get(id=topping_id)
    context = {'pizza':pizza ,'topping': topping}
    return render(request, 'pizzas/topping.html', context)

#!/usr/bin/python3
my_pizzas = ['mussarela', 'portuguesa', 'marguerita']
friend_pizzas = my_pizzas[:]

my_pizzas.append('frango com catupiry')
friend_pizzas.append('calabreza')

print("Minhas pizzas favoritas são:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nAs pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
    print(pizza.title())

#!/usr/bin/python3
lista = []

lista.append('Anderson')
lista.append('Patricia')
lista.insert(0, 'Gabriel')
del lista[1]
popped_item = lista.pop()
print(lista)
print(popped_item)

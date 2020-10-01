#!/usr/bin/python3

favorite_places = {
    'jose': 'las vegas',
    'maria': 'porto seguro',
    'katarina': 'paris',
    }

for name, place in favorite_places.items():
    print(f"O lugar favorito de {name.title()} é {place.title()}.")

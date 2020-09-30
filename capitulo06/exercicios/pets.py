#!/usr/bin/python3

rex = {
    'tipo': 'cachorro',
    'nome do dono': 'augusto',
    'idade': 5,
    }
cloe = {
    'tipo': 'gato',
    'nome do dono': 'marisa',
    'idade': 3
    }
chico = {
    'tipo': 'papagaio',
    'nome do dono': 'ricardo',
    'idade': 4,
    }
halph = {
    'tipo': 'hamister',
    'nome do dono': 'vinicius',
    'idade': 2,
    }
nadine = {
    'tipo': 'cobra',
    'nome do dono': 'lucio',
    'idade': 10
    }
pets = [rex, cloe, chico, halph, nadine]

for pet in pets:
    print(f"\nNome: {pet.title()}")
    for k, v in pet.items():
        print()

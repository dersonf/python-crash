#!/usr/bin/python3

pet_0 = {
    'nome': 'rex',
    'tipo': 'cachorro',
    'nome do dono': 'augusto',
    'idade': 5,
    }
pet_1 = {
    'nome': 'cloe',
    'tipo': 'gato',
    'nome do dono': 'marisa',
    'idade': 3
    }
pet_2 = {
    'nome': 'chico',
    'tipo': 'papagaio',
    'nome do dono': 'ricardo',
    'idade': 4,
    }
pet_3 = {
    'nome': 'halph',
    'tipo': 'hamister',
    'nome do dono': 'vinicius',
    'idade': 2,
    }
pet_4 = {
    'nome': 'nadine',
    'tipo': 'cobra',
    'nome do dono': 'lucio',
    'idade': 10
    }
pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print()
    for k, v in pet.items():
        if k == 'idade':
            print(f"{k.title()}: {v}")
        else:
            print(f"{k.title()}: {v.title()}")

#!/usr/bin/python3
# Melhoria de people.py

pessoas = {
    'mathias': {
        'nome': 'mathias',
        'sobrenome': 'silva',
        'idade': 32,
        'cidade': 'são paulo',
        },
    'madruga': {
        'nome': 'madruga',
        'sobrenome': 'santos',
        'idade': 50,
        'cidade': 'bahia',
        },
    'jose': {
        'nome': 'jose',
        'sobrenome': 'firmino',
        'idade': 25,
        'cidade': 'paraná',
        },
    }

for pessoa, infos in pessoas.items():
    print()
    for info, dado in infos.items():
        if info == 'idade':
            print(f"{info.title()}: {dado}")
        else:
            print(f"{info.title()}: {dado.title()}")

#!/usr/bin/python3

person_0 = {
    'first_name': 'mathias',
    'last_name': 'silva',
    'age': 32,
    'cidade': 'são paulo',
    }
person_1 = {
    'first_name': 'madruga',
    'last_name': 'santos',
    'age': 50,
    'cidade': 'bahia',
    }
person_2 = {
    'first_name': 'jose',
    'last_name': 'firmino',
    'age': 25,
    'cidade': 'paraná',
    }
people = [person_0, person_1, person_2]

for person in people:
    for k, v in person.items():
        if k == 'first_name':
            print(f"Nome: {v.title()}")
        if k == 'last_name':
            print(f"Sobrenome: {v.title()}")
        if k == 'age':
            print(f"Idade: {v}")
        if k == 'cidade':
            print(f"Cidade: {v.title()}\n")

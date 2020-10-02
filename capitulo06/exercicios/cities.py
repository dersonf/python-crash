#!/usr/bin/python3

cities = {
    'são paulo': {
        'pais': 'brasil',
        'populacao': '12,18 milhões',
        'fato sobre': 'O maior destino turístico brasileiro.',
        },
    'nova york': {
        'pais': 'estados unidos',
        'populacao': '8,39 milhões',
        'fato sobre': 'A primeira pizzaria dos EUA apareceu em Nova York.',
        },
    'sydney': {
        'pais': 'australia',
        'populacao': '5,23 milhões',
        'fato sobre': 'No inverno é montado uma pista de patinação na praia.',
        },
    }

for cidade, info_cidade in cities.items():
    print(f"\nCidade: {cidade.title()}")
    for info, dado in info_cidade.items():
        if info == 'fato sobre':
            print(f"\t{info.title()}: {dado}")
        else:
            print(f"\t{info.title()}: {dado.title()}")

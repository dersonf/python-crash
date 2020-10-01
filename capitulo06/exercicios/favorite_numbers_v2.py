#!/usr/bin/python3

favorite_numbers = {
    'arlindo': [7, 18],
    'paulo': [24, 69],
    'silas': [88, 15],
    'jennifer': [79, 35],
    'jose': [44, 22],
    }

for k, v in favorite_numbers.items():
    print()
    print(f"O números favoritos de {k.title()} são ", end='')

    for indice, numero in enumerate(v):
        #print(f"{numero} e ", end='')
        if indice == 0:
            print(f"{numero} e ", end="")
        else:
            print(f"{numero}.")

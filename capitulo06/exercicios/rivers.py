#!/usr/bin/python3

rivers = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangtze': 'china',
    }

for rio, pais in rivers.items():
    print(f"O {rio.title()} corre pelo {pais.title()}.")
print()

for rio in rivers.keys():
    print(rio.title())
print()

for pais in rivers.values():
    print(pais.title())

#!/usr/bin/python3

numeros = list(range(1, 10))

for numero in numeros:
    if numero == 1:
        print(f"{numero}st")
    elif numero == 2:
        print(f"{numero}nd")
    elif numero == 3:
        print(f"{numero}rd")
    else:
        print(f"{numero}th")

#!/usr/bin/python3
from random import choice

palavras = ['helicoptero', 'tamandua', 'giroscopio', 'janela']
escolhida = choice(palavras)

print(escolhida)

for i in escolhida:
    escolha = str(input('Digite uma letra: '))
    print(i)
    if escolha == i:
        print('Tem essa letra')

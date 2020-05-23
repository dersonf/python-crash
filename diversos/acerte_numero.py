#!/usr/bin/python3
from random import randrange

escolha = int(input('Qual número eu escolhi? (entre 1 e 6): '))
computador = int(randrange(1, 7, 1))
contador = 1

while escolha != computador:
    print(f'Errou, na { contador }ª tentativa, tente novamente.')
    contador += 1
    escolha = int(input('Qual número eu escolhi? (entre 1 e 6): '))

print(f'Você acertou!!! Eu escolhi o número {escolha}')
print(f'Você tentou { contador } vezes.')

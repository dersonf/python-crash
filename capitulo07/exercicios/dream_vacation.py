#!/usr/bin/python3

respostas = {}

polling_active = True

while polling_active:
    nome = input("Qual é o seu nome? ")
    lugar = input("Qual lugar no mundo desejaria conhecer? ")
    respostas[nome] = lugar

    continuar = input("Deseja continuar a enquete? (s/n): ")
    if continuar == 'n':
        polling_active = False

print("--- Resultado da pesquisa!!! ---")
for nome, lugar in respostas.items():
    print(f"{nome.title()} gostaria de conhecer {lugar}.")

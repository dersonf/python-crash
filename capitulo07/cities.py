#!/usr/bin/python3

prompt = "\nPor favor insira o nome da cidade que você visitou:"
prompt += "\n(Insira 'sair' quando você terminar.)"

while True:
    city = input(prompt)

    if city == 'sair':
        break
    else:
        print(f"Eu adorei ir para {city.title()}!")

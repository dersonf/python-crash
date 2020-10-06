#!/usr/bin/python3

prompt = "\nDigite a idade: "
prompt += "\nDigite 'sair' para encerrar."
active = True


while active:
    idade = input(prompt)
    if idade == 'sair':
        active = False
    else:
        idade = int(idade)
        if idade < 3:
            print("A entrada gratuíta.")
        elif idade <= 12:
            print("A entrada custá $10.")
        else:
            print("A entrada custa $15.")

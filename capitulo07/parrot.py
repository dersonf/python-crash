#!/usr/bin/python3

prompt = "\nDiga alguma coisa que eu repito isso pra você: "
prompt += "\nPara sair digite sair. "

active = True
while active:
    message = input(prompt)
    if message == 'sair':
        active = False
    else:
        print(f"\nPapagaio: {message}")

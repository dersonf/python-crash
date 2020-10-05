#!/usr/bin/python3

prompt = "\nDiga alguma coisa que eu repito isso pra você: "
prompt += "\nPara sair digite sair. "
message = ""
while message != 'sair':
    message = input(prompt)
    if message != 'sair':
        print(f"\nPapagaio: {message}")

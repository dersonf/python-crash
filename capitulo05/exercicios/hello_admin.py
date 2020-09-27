#!/usr/bin/python3

users = ['anderson', 'patricia', 'luiza', 'gabriel', 'admin']
#users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Olá {user}, gostaria de ver o relatório de status?")
        else:
            print(f"Olá {user.title()}, obrigado por fazer o login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")

#!/usr/bin/python3

file = 'convidados.txt'


def verifica_convidado(nome):
    with open(file) as file_object:
        nomes = file_object.readlines()
    for convidado in nomes:
        if nome == convidado.rstrip():
            print(f"Bem vindo de volta {nome}!")
        else:
            cadastra(nome)


def cadastra(nome):
    with open(file, 'a') as file_object:
        file_object.write(nome + "\n")
        print(f"Bem vindo {nome}")


if __name__ == '__main__':
    print("Para encerrar digite 'xau'")
    while True:
        nome = input("Digite um nome: ")
        if nome == 'xau':
            break
        verifica_convidado(nome)

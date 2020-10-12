#!/usr/bin/python3


def make_shirt(tamanho, frase):
    """Exibe o tamanho e a mensagem na camiseta."""
    print(f"\nA camiseta tamanho {tamanho.upper()} tem a frase:")
    print(frase)


make_shirt('m', 'Farol alta na cara é igual mulher gritando no ouvido.')
make_shirt(
    tamanho='m',
    frase='Farol alta na cara é igual mulher gritando no ouvido.',
    )
make_shirt(
    frase='Farol alta na cara é igual mulher gritando no ouvido.',
    tamanho='m',
    )

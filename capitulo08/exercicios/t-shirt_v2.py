#!/usr/bin/python3


def make_shirt(tamanho='G', frase='I amo Pyhton'):
    """Exibe o tamanho e a mensagem na camiseta."""
    print(f"\nA camiseta tamanho {tamanho.upper()} tem a frase:")
    print(frase)


make_shirt()
make_shirt('M')
make_shirt('M', 'Eu amo minha esposa e filhos.')

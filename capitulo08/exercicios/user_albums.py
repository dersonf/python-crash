#!/usr/bin/python3


def make_album(artista, album):
    """Retorna um dicionário do album."""
    dic_album = {'artista': artista, 'album': album}
    return dic_album


while True:
    print("\nInsira o artista ou banda e o album")
    print("(Para sair digite 'sair' a qualquer momento)")

    var_artista = input("Artista/Banda: ")
    if var_artista == 'sair':
        break
    var_album = input("Album: ")
    if var_album == 'sair':
        break

    album = make_album(var_artista, var_album)
    print(album)

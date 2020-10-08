#!/usr/bin/python3


def make_album(artist, titulo):
    """Retorna o artista e o album."""
    album = {'artista': artist.title(), 'album': titulo.title()}
    return album

print(make_album('madonna', 'erotica'))
print(make_album('jennifer lopez', 'on the 6'))
print(make_album('alanis morissette', 'city of angels'))

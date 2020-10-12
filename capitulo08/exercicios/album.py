#!/usr/bin/python3


def make_album(artist, titulo, songs=None):
    """Retorna o artista e o album."""
    album = {'artista': artist.title(), 'album': titulo.title()}
    if songs:
        album['songs'] = songs
    return album


print(make_album('madonna', 'erotica'))
print(make_album('jennifer lopez', 'on the 6'))
print(make_album('alanis morissette', 'city of angels'))
print(make_album('the black eyed peas', 'elephunk', 15))

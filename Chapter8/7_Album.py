def make_album(artist, album, track=''):
    album = {
        "Artist": artist,
        "Album" : album
    }
    if track != '':
        album["track"] = track
    return album

album = make_album("Bob Marley", "JAlbum")
print(album)
print()

album = make_album("Bob Marley", "JAlbum", 12)
print(album)

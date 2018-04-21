def make_album(artist, album, track=''):
    album = {
        "Artist": artist,
        "Album" : album
    }
    if track != '':
        album["track"] = track
    return album


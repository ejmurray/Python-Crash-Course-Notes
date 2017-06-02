def make_album(artist, title):
    '''Return a dictionary describing a music album
       including artist, title and number of tracks
       if known. Using a while loop.'''
    return {'Artist': artist.title(), 'Album Title': title.title()}


while True:
    print("\nPlease enter the album artists name:")
    print("\nenter 'q' at any time to quit!")

    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break

    album_title = input("Album Title: ")
    if album_title == 'q':
        break

    album_info = make_album(artist_name, album_title)
    print(album_info)

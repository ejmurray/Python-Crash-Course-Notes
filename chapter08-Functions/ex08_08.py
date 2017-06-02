def make_album(artist, title, tracks=0):
    '''Return a dictionary describing a music album
       including artist, title and number of tracks
       if known. Using a while loop.'''
    album_dict = {'Artist': artist.title(), 'Album Title': title.title()}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


print("\nPlease enter the album artists name:")
print("\nenter 'q' at any time to quit!")

while True:
    artist = input("Artist Name: ")
    if artist == 'q':
        break

    title = input("Album Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

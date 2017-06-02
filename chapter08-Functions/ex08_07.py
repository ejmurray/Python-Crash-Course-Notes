def make_album(artist, title, number_of_tracks=0):
    '''Return a dictionary describing a music album
       including artist, title and number of tracks
       if known.'''
    if number_of_tracks:
        album_info = {'Artist': artist.title(),
                      'Album Title': title.title(),
                      'Number of tracks': number_of_tracks,
                      }
    else:
        album_info = {'Artist': artist.title(),
                      'Album Title': title.title(),
                      }
    return album_info


print(make_album("snoop dogg", "gin 'n' juice", 14))
print(make_album("Wu tang gang", "36 chambers"))
print(make_album("de la soul", "pain", 12))

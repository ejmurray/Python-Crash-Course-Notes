favorite_places = {
    'ed': ['yorkshire', 'london', 'derby'],
    'carol': ['california', 'tokyo', 'berlin'],
    'david': ['jamaica', 'london', 'new york', 'liverpool'],
}

for name, places in favorite_places.items():
    print("\n {} likes the following places:".format(name.title()))
    for place in places:
        print("\t- {}".format(place.title()))

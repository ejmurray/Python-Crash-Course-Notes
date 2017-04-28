pets = []

pet = {
    'animal type': 'python',
    'name': 'jonas',
    'owner': 'katie',
    'weight': 20,
    'eats': 'rats',
}
pets.append(pet)

pet = {
    'animal type': 'rat',
    'name': 'roland',
    'owner': 'ted',
    'weight': 5,
    'eats': 'cheese',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'snoop',
    'owner': 'method man',
    'weight': 80,
    'eats': 'burgers',
}
pets.append(pet)

for pet in pets:
    print("Here's what I know about {}:".format(pet['name'].title()))
    for k, v in pet.items():
        print("\t{}: {}".format(k.title(), str(v)))

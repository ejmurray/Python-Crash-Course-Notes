def show_magicians(magicians):
    """Prints the name of each magician in a list."""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Adds the word 'Great' to the magicians name."""
    # build a new list to hold the great magicians.
    great_magicians = []

    # make each magician great and add it to great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['Harry Houdini', 'David Blaine', 'Teller', 'Dynamo']
show_magicians(magicians)
print("\n")
make_great(magicians)
show_magicians(magicians)

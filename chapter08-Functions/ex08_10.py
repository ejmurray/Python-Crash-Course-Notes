def show_magicians(greeted_magicians_names):
    """Prints the name of each magician in a list"""
    for magicians_name in magicians_names:
        print(magicians_name)


def make_great(magicians_names):
    """Adds the word 'Greet' to the magicians name"""
    for magician in magicians_names:
        add_great = "Great" + magician


magicians_names = ['Donald', 'Paul', 'Rene']
show_magicians(make_great)

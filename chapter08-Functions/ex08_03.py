"""A function that accepts the size and text on a t-shirt"""


def make_shirt(size, text):
    """Display the size and message on a t-shirt"""
    print("\nThe size of the t-shirt is {}.".format(size))
    print("The message on the shirt will say - '{}'".format(text.title()))


print(make_shirt(3, 'I love basketball!'))
print(make_shirt(size='XL', text='I love football'))

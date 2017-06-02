"""A function that accepts the size and text on a t-shirt"""


def make_shirt(size='L', text='I love python'):
    """Display the size and message on a t-shirt"""
    print("\nThe size of the t-shirt is {}.".format(size))
    print("The message on the shirt will say - '{}'".format(text.title()))


print('Default')
print(make_shirt())
print('\nDifferent size')
print(make_shirt(size='M'))
print('\nAny entry')
print(make_shirt(size='XL', text='I love football'))

"""
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the
function call provides, and it should print a summary of the sandiwch that
is being ordered. Call the function three times, using a different
number of arguments each time.
"""


def make_sandwich(*items):
    """Make a sandwich with a list of given items"""
    print("\nI'll make you a sandwich.")
    for item in items:
        print(" .....adding {} to your sandwich.".format(item))
    print("Your sandwich has been made.")


make_sandwich('salad', 'ham', 'cheese')
make_sandwich('salami', 'horseradish', 'cheese')
make_sandwich('peanut-butter', 'jam', '')

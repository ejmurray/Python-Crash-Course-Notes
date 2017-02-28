"""
Takes in the first and last name and returns a neatly formatted full name.
"""


def get_formatted_name(first, last):
    """Generate a neatly formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()

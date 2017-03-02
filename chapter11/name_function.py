"""
Takes in the first and last name and returns a neatly formatted full name.
Updated to include a middle name and to see what happens to the unitest.
"""


def get_formatted_name(first,  last, middle=''):  # the middle name here is optional
    """Generate a neatly formatted full name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

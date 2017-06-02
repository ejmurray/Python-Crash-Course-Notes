def get_formatted_name(first_name, last_name, middle_name=''):
    """
    Return a full name, neatly formatted.
    an optional argument is at the end.
    middle_name evaluates to True if a middle name is present
    in the function argumets.
    Note that the optional arg is at the end and empty.
    """
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musican = get_formatted_name('jimi', 'hendrix')
print(musican)

musican = get_formatted_name('snoop', 'dogg', 'Calvin')
print(musican)

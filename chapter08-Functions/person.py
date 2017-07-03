"""Takes textual information and adds it to a dictionary"""


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


if __name__ == '__main__':
    musician = build_person('jimi', 'hendrix', age=27)
    print(musician)

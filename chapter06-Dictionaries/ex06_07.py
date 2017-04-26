person_id_1 = {
    'first_name': 'Adam',
    'last_name': 'Smith',
    'age': 34,
    'city': 'Leeds',
}

person_id_2 = {
    'first_name': 'Busta',
    'last_name': 'Smith',
    'age': 24,
    'city': 'New York',
}

person_id_3 = {
    'first_name': 'Snoop',
    'last_name': 'Dogg',
    'age': 34,
    'city': 'Leeds',
}

people = [person_id_1, person_id_2, person_id_3]

for person in people:
    for k, v in person.items():
        print("\n{}: {}".format(k.title(), v))

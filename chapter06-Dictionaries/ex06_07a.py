people = []

person = {
    'first_name': 'snoop',
    'last_name': 'dogg',
    'age': 40,
    'city': 'Los Angeles',
}

people.append(person)

person = {
    'first_name': 'klay',
    'last_name': 'thompson',
    'age': 24,
    'city': 'California',
}

people.append(person)

person = {
    'first_name': 'barack',
    'last_name': 'obama',
    'age': 56,
    'city': 'Catskill',
}

person.append(people)

name = person['first_name'] + " " + person["last_name"]

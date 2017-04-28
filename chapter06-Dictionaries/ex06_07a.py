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
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person["last_name"].title()
    age = str(person['age'])
    city = person['city'].title()
    print("Hi {}. You are aged {} and live in {}.".format(name, age, city))


person_id = {
    'first_name': 'Adam',
    'last_name': 'Smith',
    'age': 34,
    'city': 'Leeds',
}
# this prints an unordered list
for key, value in person_id.items():
    print(key.title() + ": " + str(value))

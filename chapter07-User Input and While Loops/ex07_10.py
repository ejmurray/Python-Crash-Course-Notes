"""
Dream vacation
Write a program that polls users about their dream vacation.
Write a prompt similar to the one in 'If you could visit one
place in the world, where would it be?' Include a block of
code that prints the results of the poll.
"""

name_prompt = "\nWhat is your name? "
place_prompt = "Where would you like to visit in the world? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Response is stored in a dict
responses = {}

while True:
    # Ask the user questions
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response
    responses[name] = place

    # Ask if there is anyone else wanting to respond
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

print('\n-----Results-----')
for name, place in responses.items():
    print('{} would like to visit {}.'.format(name.title(), place.title()))

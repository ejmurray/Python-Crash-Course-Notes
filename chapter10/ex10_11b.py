"""
Part 2.
Write a program that prompts for the user’s favorite
number Use json.dump() to store this number in a file.
Write a separate program that reads in this value and prints the message,
“I know your favorite number! It’s _____ ”
"""

import json

filename = 'favorite_number.json'
with open(filename) as f:
    display_number = json.load(f)
    print("Your favorite number is: {}.".format(display_number))

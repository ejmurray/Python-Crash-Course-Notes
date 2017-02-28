"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""
import json

filename = 'favorite_number_2.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Please enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print("Your favourite number {} has been stored.".format(favorite_number))
else:
    print("Your favorite number is, {}.".format(favorite_number))


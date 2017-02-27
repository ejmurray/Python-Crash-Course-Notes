"""
Write a program that prompts for the user’s favorite
number Use json.dump() to store this number in a file.
Write a separate program that reads in this value and prints the message,
“I know your favorite number! It’s _____ ”
"""
import json

filename = 'favorite_number.json'
favorite_number = input("Enter your favorite number? ")
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print("Your favorite number has been stored.")

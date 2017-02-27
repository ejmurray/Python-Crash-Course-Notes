"""
second version of the remember me script
"""
import json

filename = 'username.json'

try:
    with open(filename) as f:
        user = json.load(f)
except FileNotFoundError:
    user = input("Please enter your username? ")
    with open(filename, 'w') as f:
        json.dump(user, f)
        print("{}. I'll remember you the next time you login.".format(user))
else:
    print("Welcome back {}".format(user))

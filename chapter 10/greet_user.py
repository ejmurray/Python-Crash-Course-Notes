"""
Greet a user who has already been stored.
"""

import json

filename = 'username2.json'

with open(filename) as f:
    username = json.load(f)
    print("Welcome back {}!".format(username))

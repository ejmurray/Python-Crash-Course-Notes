"""
saving and reading user generated data
"""

import json

username = input("What is your name? ")

filename = 'username2.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print("We'll remember you whn you come back {}!".format(username))

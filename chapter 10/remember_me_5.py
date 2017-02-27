"""
10-13: Verify User
The final listing for remember_me.py assumes either that the user has already entered their
username or that the program is running for the first time. We should modify it in case the
current user is not the person who last used the program. Before printing a welcome back
message in greet_user(), ask the user if this is the correct username.
If it’s not, call get_new_username() to get the correct username.
"""

import json


def get_stored_username():
    """Get the stored username if it is available."""
    filename = 'username4.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username4.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by their name."""
    username = get_stored_username()
    if username:
        correct = input("Are you {}? (y/n) ".format(username))
        if correct == 'y':
            print("Welcome back {}!".format(username))
        else:
            username = get_new_username()
            print("We'll remember you when you come back, {}.".format(username))
    else:
        username = get_new_username()
        print("We'll remember you when you come back, {}.".format(username))

greet_user()

# Clean version:
# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         correct = input("Are you " + username + "? (y/n) ")
#         if correct == 'y':
#             print("Welcome back, " + username + "!")
#             return
#
#     # We got a username, but it's not correct.
#     # Let's prompt for a new username.
#     username = get_new_username()
#     print("We'll remember you when you come back, " + username + "!")

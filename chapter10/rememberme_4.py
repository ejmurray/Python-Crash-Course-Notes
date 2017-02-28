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
        print("Welcome back {}!".format(username))
    else:
        username = get_new_username()
        print("We'll remember you when you come back, {}.".format(username))

greet_user()

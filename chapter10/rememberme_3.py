import json


def greet_user():
    """Greet the user by their name"""
    filename = 'username3.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('Please enter your username? ')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print('Hi {}. Your username will be remember for the next time you logon.'.format(username))
    else:
        print('Welcome back {}'.format(username))


greet_user()

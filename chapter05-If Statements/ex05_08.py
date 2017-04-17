"""
Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Give two different greetings depending on if you are admin or a normal user.
"""

usernames = ['admin', 'ernest', 'paul', 'fred', 'max']

for username in usernames:
    if username == 'admin':
        print('Hello {}, would you like a status report?'.format(username.capitalize()))
    else:
        print('Hello {}, thank you for logging in again.'.format(username.capitalize()))

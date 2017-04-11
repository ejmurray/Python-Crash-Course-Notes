"""No User: Adding an if statement to ex 5-8 to check if a list
 is empty."""

# sernames = []
usernames = ['amir', 'admin', 'jack', 'scott', 'percy']

if usernames:  # If a list has more than one item, continue with the for loop!
    for username in usernames:
        if username is 'admin':
            print('Hello {}, would you like to see a status report?'.format(username.capitalize()))
        else:
            print('Hello {}, thank you for logging in again.'.format(username.capitalize()))
else:  # If the list is empty, go to the else loop.
    print('We need to find some users!')

banned_users = ['andrew', 'caroline', 'david']
user = 'marie'

if user not in banned_users:
    print("{}, you can post a response if you wish.".format(user.title()))

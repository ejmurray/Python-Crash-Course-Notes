favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

take_the_poll = ['jen', 'sarah', 'phil', 'paul', 'ant']


for poll in take_the_poll:
    if poll in favourite_languages:
        print('Thank you {} for taking the poll.'.format(poll.title()))
    else:
        print('{}, please take the poll.'.format(poll.title()))


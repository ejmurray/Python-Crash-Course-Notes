"""Guest book"""
filename = 'guest_book.txt'

print('Enter "quit" to fininsh!')
while True:
    name = input('\nWhat is your name? ')
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write('Guest Name: '+ name + '\n')
            print('Welcome {}. You have been added to the guest book.'.format(name))

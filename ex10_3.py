"""Guest book"""
<<<<<<< HEAD
filename = 'guest_book.txt'

print('Enter "quit" to fininsh!')
while True:
    name = input('\nWhat is your name? ')
=======
# filename = 'guest_book.txt'

# print("Enter 'quit' when you are finished.")
# while True:
#     name = ''
#     name = str(input("\nEnter your name. "))
#     if name == 'quit':
#         break
#     else:
#         with open(filename, 'a') as f:
#             f.write(name + '\n')
#         print("Hi {}, you've been added to the guest book.".format(name))


filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = str(input("\nWhat's your name? "))
>>>>>>> 4b1094d63195b248316d6e60c7e14fa337bf3bcf
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
<<<<<<< HEAD
            f.write('Guest Name: '+ name + '\n')
            print('Welcome {}. You have been added to the guest book.'.format(name))
=======
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")
>>>>>>> 4b1094d63195b248316d6e60c7e14fa337bf3bcf

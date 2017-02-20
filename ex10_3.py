"""Guest book"""

filename = "guest_book.txt"
print("Enter 'quit' when you are finished.")
while True:
    name = str(input("\nWhat's your name? "))
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write('Guest Name: '+ name + '\n')
            print('Welcome {}. You have been added to the guest book.'.format(name))
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")

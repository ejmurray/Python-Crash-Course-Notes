"""Guest book"""
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = ''
    name = str(input("\nEnter your name. "))
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + '\n')
        print("Hi {}, you've been added to the guest book.".format(name))

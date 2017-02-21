"""add two numbers together and show a TypeError if a non int is entered."""


try:
    a = input('Enter your first number: ')
    a = int(a)
    b = input('Enter a second number: ')
    b = int(b)
except ValueError:
    print("You need to enter a number!")
else:
    sum = int(a) + int(b)
    print('The sum of {} and {} is {}'.format(a, b, sum))

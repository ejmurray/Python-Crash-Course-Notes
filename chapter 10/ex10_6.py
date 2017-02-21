"""add two numbers together and show a TypeError if a non int is entered."""


try:
    a = input('Enter your first number: ')
    int(a)
    b = input('Enter a second number: ')
    int(b)
except TypeError:
    print("You need to enter a number!")
else:
    sum = int(a) + int(b)
    print('The sum of {} and {} is {}'.format(a, b, sum))

"""add two numbers together and show a TypeError if a non int is entered."""

try:
    x = input("Give me your first number: ")
    x =  int(x)

    y = input("Give me a second number: ")
    y = int(y)

except ValueError:
    print("You need to enter a number.")

else:
    sum = x + y
    print("The sum of {} and {} is {}".format(x, y, sum))

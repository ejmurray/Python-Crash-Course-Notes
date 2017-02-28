"""
add two numbers together and show a TypeError if a non int is entered.
The error in this script compared to 10_7a.py is that it is looking at the
value of x as an int when you add the letter q then ith throws the error and
you cannot get out of the loop.
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
while True:
    try:
        x = int(input("Give me your first number: "))
        if x == 'q':
            break
        y = int(input("Give me a second number: "))
        if y == 'q':
            break

    except ValueError:
        print("You need to enter a number.")

    else:
        sum = x + y
        print("The sum of {} and {} is {}".format(x, y, sum))

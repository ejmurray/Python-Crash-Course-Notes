"""add two numbers together and show a TypeError if a non int is entered."""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
while True:
    try:
        x = input("Give me your first number: ")
        if x == 'q':
            break
        x = int(x)
        y = input("Give me a second number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("You need to enter a number.")

    else:
        sum = x + y
        print("The sum of {} and {} is {}".format(x, y, sum))

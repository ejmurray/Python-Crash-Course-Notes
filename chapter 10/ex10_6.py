"""add two numbers together and show a TypeError if a non int is entered."""
print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit")

while True:
    a = input("\nFirst number: ")
    if a == 'q':
        break
    try:
        a is int == True
    except TypeError:
        print('Please enter an integer.')
    b = input("Second number: ")
    if b == 'q':
        break
    try:
        b is int == True
    except:
        print('Please enter an integer.')
    try:
        answer = int(a) / int(b)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

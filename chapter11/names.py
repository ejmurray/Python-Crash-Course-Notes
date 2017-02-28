"""Lets the user enter a first and last name and see a neatly formatted full name."""

from chapter11.name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease enter the first name: ")
    if first == 'q':
        break
    last = input("Please enter a last name: ")
    if last == 'q':
        break

formatted_name = get_formatted_name(first, last)
print("\nNeatly formatted name: " + formatted_name + '.')

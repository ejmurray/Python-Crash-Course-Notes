"""
This code is more efficient since since you only need
to change the prices and the final print statement.

Here you can use more than one elif statement too.
Use a final elif if you want to catch a specific final condition
insted of using an else statement which is a catch all case.
"""

age = 78

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10  # full admission price
elif age >= 65:
    price = 5  # this final block makes the code clearer
print("Your admision cost is £{}.".format(price))

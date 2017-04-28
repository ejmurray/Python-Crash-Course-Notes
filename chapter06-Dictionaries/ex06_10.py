"""Favorite numbers"""

favorite_numbers = {
    'ed': [3, 5, 7],
    'carol': [34, 56, 5445],
    'david': [345, 4, 6],
}

for name, numbers in favorite_numbers.items():
    print("\n {}'s favorite numbers are:".format(name.title()))
    for number in numbers:
        print("- {}".format(str(number)))

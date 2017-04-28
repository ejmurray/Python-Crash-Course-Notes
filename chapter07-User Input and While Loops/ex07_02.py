"""Restaurant seating"""

seating_numbers = input("Enter the number of guests that you will have eating with us today: ")

seating_numbers = int(seating_numbers)

if seating_numbers > 8:
    print("\nYou will have to wait for an availible table.")
else:
    print("\nYour table is ready.")

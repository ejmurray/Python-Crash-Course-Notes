# https://goo.gl/xh2avh
"""
Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class.
Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number that could represent how many customers were served in, say, a day of business.
"""


class Restaurant:
    """Here is a new class that defines restaurants."""
    def __init__(self, restaurant_name, cuisine_type):
        """Here is the inti part of the class"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type"""
        print("This restaurant is a called " + self.restaurant_name + " and it serves " + self.cuisine_type + " food.\n")

    def open_restaurant(self):
        """Prints a message that the restaurant is open."""
        print("The restaurant is open.")

    def set_number_served(self, number):
        """The number of customers served in a day."""
        self.number += number
        # print("The restaurant has served " + str(self.number) + " of people today.")

    def increment_number_served(self, additional_served):
        """Allows the user to add additional customers"""
        self.number += additional_served


restaurant = Restaurant("Thai-Phoo", "Thai")
restaurant.describe_restaurant()

print("Number of people served: " + str(restaurant.number))
restaurant.number = 20
print("Number of people served: " + str(restaurant.number))  # 20

restaurant.set_number_served(100)
print("Number of people served: " + str(restaurant.number))  # 120

restaurant.increment_number_served(105)
print("Number of people served: " + str(restaurant.number))  # 225

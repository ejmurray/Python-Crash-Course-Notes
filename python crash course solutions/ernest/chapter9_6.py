"""
9-6: Ice Cream Stand

An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166)
or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""


class Restaurant:
    """This class is used to describe a restaurant"""

    def __init__(self, restaurant_name, cuisine):
        """Create an instance of a restaurant"""
        self. restaurant_name = restaurant_name.title()
        self.cuisine = cuisine
        self.visitors = 0

    def describe_restaurant(self):
        """a method to describe the restaurant"""
        print(self.restaurant_name + " is a restaurant that serves " + self.cuisine + " food\n")

    def open_restaurant(self):
        """Welcome message to tell you that it is open"""
        print("Welcome to our restaurant.")

    def number_served(self, visitors):
        """Records the number of visitors to the restaurant"""
        self.visitors += visitors

    def increment_visitors(self, served):
        """increments the number of patrons that have visited"""
        self.visitors += served


class IceCreamStand (Restaurant):
    """A specific type of restaurant that inherits from the Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type='ice-cream'):
        """
        initialise attributes of the parent class .
        Then initialise attributes specific to the IceCreamStand
        :param restaurant_name:
        :param cuisine_type:
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def display_flavours(self):
        """Displays the flavours of ice cream on offer"""
        print("Today we are serving:")
        for f in self.flavours:
            print("- " + f.title())

cross_gates = IceCreamStand("Cross Gates Lhasi")
cross_gates.flavours = ["vanilla", "strawberry", "mint"]
cross_gates.describe_restaurant()
cross_gates.display_flavours()

# thailand = Restaurant("Thai-Phoo", "Thai")
# print(thailand.describe_restaurant())

# thailand.visitors = 50
# print("The number of people served today is: " + str(thailand.visitors))
# thailand.increment_visitors(10)
# print("The number of people served today is: " + str(thailand.visitors))
# thailand.increment_visitors(100)
# print("The number of people served today is: " + str(thailand.visitors))

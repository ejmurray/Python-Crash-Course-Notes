# https://goo.gl/xh2avh


class Restaurant:
    """Here is a new class that defines restaurants."""
    def __init__(self, restaurant_name, cuisine_type):
        """Here is the inti part of the class"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type"""
        print("This restaurant is a called " + self.restaurant_name + " and it serves " + self.cuisine_type + " food." + '\n')

    def open_restaurant(self):
        """Prints a message that the restaurant is open."""
        print("The restaurant is open.")


# restaurant = Restaurant("Burger King", "Greasy Food")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# From the website

# class Restaurant:
#     """A class representing a restaurant."""
#
#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = self.name + " serves wonderful " + self.cuisine_type + "."
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = self.name + " is open. Come on in!"
#         print("\n" + msg)
#
# restaurant = Restaurant('the mean queen', 'pizza')
# print(restaurant.name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
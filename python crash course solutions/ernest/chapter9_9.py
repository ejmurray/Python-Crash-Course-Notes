"""
9-9: Battery Upgrade

Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery().
This method should check the battery size and set the capacity to 85
if it isn’t already. Make an electric car with a default battery size,
call get_range() once, and then call get_range() a second time after upgrading
the battery. You should see an increase in the car’s range.
"""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialise attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on the clock.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Naughty. You cannot roll back an odometer!")

    def increment_odometer(self, miles):
        """Add a given amount to the odometer reading."""
        self.odometer_reading += miles




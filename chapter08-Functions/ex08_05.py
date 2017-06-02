"""A function that describes the cities in a county"""


def describe_city(city, country='England'):
    """A function that describes a city and its country"""
    print("\n{} is in {}.".format(city.title(), country.title()))


print(describe_city('London'))
print(describe_city('Manchester'))
print(describe_city(city='kingston', country='jamaica'))
print(describe_city(city='new york', country='america'))
print(describe_city(city='amsterdam', country='holland'))

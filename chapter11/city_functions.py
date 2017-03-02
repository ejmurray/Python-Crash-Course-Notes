"""Write a function that accepts two parameters: a city name
and a country name. the function should return a single string in
the form City, Country, such as Santiago, Chile. Store the function in a
module called city_functions.py

Cheated in the test since the word population is capitalised using the title case in the
returned module.
This solution is different to the one suggested in the text.
"""


def city_functions(city, country, population=0):  # note that population is an int and doesn't need the ''
    """Returns a single string in the form City, Country"""
    if population:
        full_name = city + ', ' + country + ' - population ' + str(population)
    else:
        full_name = city + ', ' + country + '.'
    return full_name.title()

a = city_functions('Santiago', 'Chile')
print(a)

b = city_functions('Santiago', 'Chile', 5000000)
print('\n' + b)

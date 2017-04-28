"""Cities"""

cities = {
    'manchester': {
        'country': 'england',
        'population': 3000000,
        'nearby mountains': 'Penny Gent',
    },
    'bangor': {
        'country': 'wales',
        'population': 50000,
        'nearby mountains': 'snowden',
    },
    'london': {
        'country': 'england',
        'population': 10000000,
        'nearby mountains': 'brecon beacons',
    },
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n{} is in {}.".format(city.title(), country))
    print(" It has a population of {}".format(population))
    print(" The mountain called {} is nearby.".format(mountains))

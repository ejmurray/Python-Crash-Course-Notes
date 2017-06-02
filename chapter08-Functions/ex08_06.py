def city_country(city, country):
    '''Print out the city and country in a simple format'''
    formatted_text = city.title() + ', ' + country.title()
    return formatted_text

print(city_country('leeds', 'uk'))
print(city_country('santiago', 'chile'))
print(city_country('kingston', 'jamaica'))

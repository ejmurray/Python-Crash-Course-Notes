favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favourite language is {}."
      .format(favourite_languages['sarah'].title()))
print('\n')
for name, language in favourite_languages.items():
    print("{}'s favourite language is {}.".format(name.title(), language))


# looping through all keys.

print("\n")
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi {}, I see that your favourite language is {}".format(name.title(), favourite_languages[name].title()))

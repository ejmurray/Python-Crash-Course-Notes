favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# looping through all keys.
# If the name is in the friends list then a special message is added.

print("\n")
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi {}, I see that your favourite language is {}".format(name.title(), favourite_languages[name].title()))


# Using the keys method to find out if a person was polled.
# Does the person exist in the dictionary?

if 'erin' not in favourite_languages.keys():
    print("\nErin, please take our poll!")

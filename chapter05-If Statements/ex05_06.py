"""
Stages of life: determines a ages age.
"""

age1 = 17
age = age1

if age <= 2:
    age = 'baby'
elif age <= 4:
    age = 'toddler'
elif age <= 13:
    age = 'kid'
elif age <= 20:
    age = 'teenager'
elif age <= 65:
    age = 'adult'
else:
    age = 'elder'
if age.startswith('a') or age.startswith('e'):
    print('You are a {} years old and therefore are an {}'.format(age1, age))
else:
    print('You are a {} years old and therefore are a {}'.format(age1, age))

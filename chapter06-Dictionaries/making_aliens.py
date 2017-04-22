aliens = []

for alien_number in range(30):
    new_alien = {'colour': 'green',
                 'points': 5,
                 'speed': 'slow',
                 }
    aliens.append(new_alien)

# Changing the colour of the first three.
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':  # Expanding the loop
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first five aliens.
print('Printing the first five aliens.')
for alien in aliens[:5]:
    print(alien)
print('....')

# Show how many aliens have been created.
print('Total number of aliens created: {}'.format(len(aliens)))

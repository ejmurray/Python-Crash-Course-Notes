alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("\nYou just earned {} points!".format(new_points))
# adding new key, value pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print('Updated dictionary')
print(alien_0)

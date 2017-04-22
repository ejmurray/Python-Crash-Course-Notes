# Tracking the position of an alien.

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: {}".format(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on the speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # A fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] += x_increment
print("\nNew position: {}".format(alien_0['x_position']))

'''reading file contents.'''
filename = 'pi_digits.txt'

with open(filename) as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print('')
print('The lenght of pi_string is {}'.format(len(pi_string)))

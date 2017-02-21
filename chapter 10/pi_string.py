filename = 'pi_million_digits.txt'

with open(filename) as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + '...')
print('')
print('Here are the first 52 digits of pi\'s {} digits.'.format(len(pi_string)))
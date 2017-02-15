filename = 'pi_million_digits.txt'

with open(filename) as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = str(input('Please enter your birthday, in the form ddmmyy: '))
if birthday in pi_string:
    print('Your birthday appers in the milliion digits of pi')
else:
    print('Your birthday does not appear in the million digits of pi.')

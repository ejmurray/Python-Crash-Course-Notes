"""
Ordinal numbers indicate  their position in a list, such sd 1st, 2nd.
The rest end in th. Store numbers 1-9 in a list. Loop through the list.
Using an if-elif-else chain inside tje loop to print the proper ordinal
number. The input should read 1st, 2nd 3rd etc. Each result should be
on a seperate line.
"""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in number_list:
	if i == 1:
		print('1st')
	elif i == 2:
		print('\n2nd')
	elif i == 3:
		print('\n3rd')
	else:
		print('\n{}th'.format(i))

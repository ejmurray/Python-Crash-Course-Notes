# looking at rivers in england

rivers = {
	'nidd': 'knaresborough',
	'calder': 'leeds',
	'humber': 'hull',
	'colne': 'derbyshire',
	'foss': 'york',
}

print('Names of rivers:\n')
for river in sorted(rivers.keys()):
	print('{}'.format(river.title()))

print('\nWhere are the rivers?\n')
for city in sorted(rivers.values()):
	print('{}'.format(city.title()))

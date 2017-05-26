'''Using positional arguments'''

def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a {}.".format(animal_type))
	print("My {}'s name is {}.".format(animal_type, pet_name.title()))


describe_pet('dog', 'barney')
describe_pet('hamster', 'polly')

'''Here is the function with keyword arguments'''
def describe_pet2(pet_name, animal_type='dog'):
	"""Display information about a pet dog with keyword arg"""
	print("\nI have a {}.".format(animal_type))
	print("My {}'s name is {}. Done with the keyword argument.".format(animal_type, pet_name.title()))

describe_pet2('rip-up')
describe_pet2(pet_name='mary', animal_type='horse')

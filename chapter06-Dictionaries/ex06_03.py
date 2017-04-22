# Glosssary of python terms

python_terms = {
    'dictionary': 'has curly braces and uses key value pairs.',
    'list': 'has square brackets and is mutable.',
    'string': 'a collection of letters and numbers.',
    'int': 'numbers from 0 to 9.',
    'tuple': 'immutable list. Think of theses like co-ordinates that do not change.',
    'truthiness': 'a value can be true or false.',
    'str.capitalize()': 'capitalizes the first letter of a sentence.',
}

for k, v in python_terms.items():
    print(k.title() + ": " + v.capitalize())

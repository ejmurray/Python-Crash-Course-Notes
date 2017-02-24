"""
uses the json.load() function to read the list back into memory.
"""

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

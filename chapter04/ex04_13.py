"""Buffet. Use a tuple to represent five foods available at the restaurant."""


buffet_items = 'rice', 'mashed potatoes', 'sausages', 'chicken curry', 'spare ribs'
print('Here is the original buffet:\n')
for i in buffet_items:
    print(i.title())

# Attempt to change one of the items in the tuple using its index position.
# buffet_items[0] = 'cheese'

# The menu has two items that have been replaced. Add them to the tuple.
buffet_items = 'rice', 'burrito', 'pad thai', 'chicken curry', 'spare ribs'
print('\nHere is the updated buffet:\n')
for i in buffet_items:
    print(i.title())

# In tuples you need to write a new tuple since you cannot append or replace
# an item in the same way as you do in a list. See the last example that fails.

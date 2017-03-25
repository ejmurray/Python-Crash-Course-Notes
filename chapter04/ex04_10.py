"""Here is the stuff fron ex 4-1 with three added lines."""
pizzas = ['pepperoni', 'meat feast', 'spicy hot one',
          'ham and pinapple', 'american hot one']

for pizza in pizzas:
    print('I like {} pizza'.format(pizza.title()))
print('\nI really love pizza. Yum!!!')

print("\nThe first three items in the list are: ")
for i in pizzas[:3]:
    print(i.title())
print("\nThe items in the middle of the list are: ")
for i in pizzas[1:4]:
    print(i.title())
print("\nHere's what is at the end of the list: ")
for i in pizzas[2:]:
    print(i.title())

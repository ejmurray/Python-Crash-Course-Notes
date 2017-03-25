"""My pizzas, your pizzas. Copy the pizza list and manipulate it."""

pizzas = ['pepperoni', 'meat feast', 'spicy hot one']
friends_pizzas = pizzas[:]

print("\nHere is the list of my pizzas {}".format(pizzas))
print("Here is the list of my friend's pizza {}".format(friends_pizzas))

pizzas.append('four seasons')
print("\nHere is the updated list of my pizzas {}".format(pizzas))

friends_pizzas.append('cheese and tomato')
print("Here is the updated list of my friend's pizza {}".format(friends_pizzas))

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friends favorite pizzas are:")
for f_pizza in friends_pizzas:
    print(f_pizza.title())
# print('\nI really love pizza. Yum!!!')

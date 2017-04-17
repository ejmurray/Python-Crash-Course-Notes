available_toppings = ['mushrooms', 'olives', 'green peppers', 'perpperoni',
                        'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding {} to your pizza.'.format(requested_topping))
    else:
        print("Sorry, we don't have {}.".format(requested_topping))

print("\nFinished making your pizza!")

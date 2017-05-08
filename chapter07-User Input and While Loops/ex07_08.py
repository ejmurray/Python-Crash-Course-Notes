sandwich_orders = ['ham and cheese', 'BLT', 'tuna mayo', 'peanut butter and jelly']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your {} sandwich.".format(current_sandwich.title()))
    finished_sandwich.append(current_sandwich)

print('\n')
for sandwich in finished_sandwich:
    print("I made a {} sandwich.".format(sandwich.title()))

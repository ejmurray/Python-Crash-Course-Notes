"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich
'pastrami' appears in the list at least three times. Add code near the
beginning of your program to print a message saying the deli has run
out of pastrami, and then use a while loop to remove all occurrences
of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches
end up in 'finished_sandwiches'.
"""

sandwich_orders = ['ham and cheese', 'BLT', 'tuna mayo', 'peanut butter and jelly', 'pastrami'
                  , 'pastrami', 'pastrami', 'pastrami'
                  ]
finished_sandwich = []

print("I'm sorry. The deli has run out of pastrami sandwiches.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your {} sandwich.".format(current_sandwich))
    finished_sandwich.append(current_sandwich)

print("\n")

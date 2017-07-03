def make_pizza(size, *toppings):
    """Make a pizza of a given size and with a list of toppings"""
    print("\nMaking a {} inch pizza with the following toppings".format(str(size)))
    for topping in toppings:
        print("- {}".format(topping))

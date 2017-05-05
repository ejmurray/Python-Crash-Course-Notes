"""Pizza toppings loop"""

prompt = "\nEnter the name of a pizza topping."
prompt += "(\nEnter 'quit' when you are finished.) "

topping = ""

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I'll add {} as a topping for your pizza.".format(topping))

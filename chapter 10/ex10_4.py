"""Programming Poll"""

filename = "programming_poll.txt"
responses = []

while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like someone else to add a response? (y/n)")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + '\n')

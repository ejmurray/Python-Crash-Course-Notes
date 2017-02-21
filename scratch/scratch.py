"""scratch file"""

filename = "programming_text2.txt"
responses = []

while True:
    response = input("Enter a reason why you like programming: ")
    responses.append(response)

    continue_response = input("Would you like someone else add respond? (y/n)? ")
    if continue_response != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + '\n')

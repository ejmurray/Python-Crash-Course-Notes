filename = 'learning_python.txt'
print('\nReading in the entire file.....')
with open(filename) as f:
    lines = f.read()
print(lines)

print('\nPrint using the for loop.....')
with open(filename) as f:
    for line in f:
        print(line.strip())

print("\nReading the lines using a for loop....")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

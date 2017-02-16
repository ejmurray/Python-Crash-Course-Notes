"""Using the replace function in a textfile."""
filename = 'learning_python_replace.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line.replace("Python", "C++")
    print(line.strip())


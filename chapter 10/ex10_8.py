"""
read in and print the contents of the files. Use a FileNotFoundError if the
file is missing.
"""
filenames = ['cats.txt', 'dogs.txt', 'hamsters.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        print("The file named {} is missing".format(filename))

    else:
        print("\nReading file: {}".format(filename))
        print(contents)

"""
read in and print the contents of the files. Use a FileNotFoundError if the
file is missing.
"""
filelist = ['cats.txt', 'dogs.txt', 'hamsters.txt']

for file in filelist:
    print("Reading file: {}".format(file))
    try:
        with open(file, 'r') as f:
            contents = f.read()
            print(contents)

    except FileNotFoundError:
        print("The file named {} is missing".format(file))

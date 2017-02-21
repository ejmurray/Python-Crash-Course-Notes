"""handling a FileNotFoundError error"""

filename = 'alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file: {} does not exist.".format(filename)
    print(msg)
else:
    # count the number of words in the filename
    words = contents.split()
    num_words = len(words)
    print("The file: {} has about {} words.".format(filename, str(num_words)))

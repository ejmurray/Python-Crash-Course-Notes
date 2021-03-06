# fails silently
def count_words(filename):
    """Count the approximate number of words in a file."""
    # filename = 'alice.txt'
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # count the number of words in the filename
        words = contents.split()
        num_words = len(words)
        print("The file: {} has about {} words.".format(filename, str(num_words)))

# filename = "alice.txt"
# count_words(filename)
# rename the second file with 'dd'
filenames = ['alice.txt', 'sidhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

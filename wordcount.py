def count_word_occurence(filename):
    """ Counts and prints the occurence of each word in a file."""
    # open a file
    file = open(filename)

    # define empty dictionary
    word_counts = {}

    for line in file:
        line = line.strip() # strip white space
        line = line.replace(",", "") # delete ','
        line = line.replace(".", "") # delete '.'
        line = line.replace("?", "") # delete '?'
        line = line.lower() # make all words lowercase
        words = line.split(" ") # retreive individual words from a line
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1 # add each unique word to word_counts and count them
    
    for word in word_counts:
        print(word, word_counts[word]) # print each word and its occurence

#count_word_occurence("test.txt")
#count_word_occurence("twain.txt")
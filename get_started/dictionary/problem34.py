#Improve the above program to print the words in the descending order of the number of occurrences.

def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency
def read_words(filename):
    return open(filename).read().split()

def main(filename):
	x=[]
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.items():
    	x.append((word,count))
    	x.sort()
        print word, count

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
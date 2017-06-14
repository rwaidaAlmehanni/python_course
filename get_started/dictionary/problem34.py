#Improve the above program to print the words in the descending order of the number of occurrences.
import sys


# def word_frequency(words):
#     frequency = {}
#     for w in words:
#         frequency[w] = frequency.get(w, 0) + 1
#     print frequency
import sys
def test(words): # return factorial
 x=[]
 f={}
 for w in words:
     f[w] = f.get(w, 0) + 1
 for word, count in f.items():
     x.append((word,count))
     x.sort()
 print x

test(open(sys.argv[1]).read().split())
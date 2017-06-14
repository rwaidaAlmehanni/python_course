# Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?
import sys
def test(words): 
 x=[]
 f={}
 for w in words:
   [c for c in w]
   for i in c:
     f[i] = f.get(i, 0) + 1
 for word, count in f.items():
     x.append((word,count))
     x.sort()
 print x[::-1]

test(open(sys.argv[1]).read().split())
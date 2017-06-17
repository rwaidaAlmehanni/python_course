#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively

import sys
from os import listdir
def readLineChar():
  f={}
  x=listdir(sys.argv[1])
  for i in x:
  	f[i]=len(open(i).readlines())
  print f

readLineChar()


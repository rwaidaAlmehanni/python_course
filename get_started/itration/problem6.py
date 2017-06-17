#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively

import sys
from os import listdir
def readLineChar():
  f={}
  counter=0;
  x=listdir(sys.argv[1])
  for i in x:
  	if str(i).index(".")!=[0]:
  		for j in open(i).readlines():
  			if j!=" " and j[0]!="#":
  				counter+=1;
        f[str(i)]=counter;
        counter=0;        
  print f

readLineChar()


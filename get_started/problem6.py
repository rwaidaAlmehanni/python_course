#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively

import sys
from os import listdir
def readFileLines(xfile):
    counter=0
    for i in open(xfile).readlines():
      if i!="\n" and i[0]!="#":
        counter+=1
    return counter             


def readDirFiles():
    f={}
    y=0
    x=listdir(sys.argv[1])
    for i in x:
      if "." in str(i):
        y=readFileLines(sys.argv[1]+"/"+i)
        f[str(i)]=y		 
    print f

readDirFiles()


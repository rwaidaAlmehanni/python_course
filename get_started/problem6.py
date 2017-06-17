#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively

import sys
def readFileLines(xfile):
  f={}
  counter=0
  for i in open(xfile).readlines():
    if i!="\n" and i[0]!="#":
      counter+=1
  f[str(xfile)]=counter

  print f             


def readDirFiles():
  f=[]
  x=listdir(sys.argv[1])
  for i in x:
  	if str(i).index(".")!=0:
      f.append(readFileLines(i))		 
  print f

readDirFiles()


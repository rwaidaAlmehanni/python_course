# Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension
import sys
from os import listdir
def listDir():
  f={}
  x=listdir(sys.argv[1])
  for i in x:
    ind=i.index(".")
    f[i[ind+1:]]=f.get(i[ind+1:],0)+1
  print f

listDir()
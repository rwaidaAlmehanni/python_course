# Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.
import sys
from os import listdir
def listdirx():
  r={}
  res=[]
  x = listdir(sys.argv[1])
  for i in x:
    r["Last-Modified"]=i.headers["Last-Modified"]
    r["Content-Length"]=i.headers["Content-Length"]
    r["Content-Type"]=i.headers["Content-Type"]
    res.append(r)
    r=[]
  print res

listdirx()




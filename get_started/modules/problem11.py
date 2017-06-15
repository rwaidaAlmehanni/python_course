# Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.
import zipfile
import sys
def writeFile():
  zf = zipfile.ZipFile(sys.argv[1])                     
  zf.write(sys.argv[2])
  zf.close()
  for x in zf.namelist():
    print zf.read(x) 
 
writeFile()   
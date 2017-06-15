#Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
import sys
import tablib
def csv2xls():
   data = tablib.Dataset()
   data.append(open(sys.argv[1]).read())
   with open('test.xls', 'wb') as f:
	f.write(data.xls) 
   print "done"

csv2xls()
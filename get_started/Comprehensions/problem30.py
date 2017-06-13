# Write a python function parse_csv to parse csv (comma separated values) files.
import sys
def openf():
	return open(sys.argv[1]).read()

def parse_csv(f):
	y=f.split("\n")
	print [x.split(",") for x in y]
 
parse_csv(openf()) 
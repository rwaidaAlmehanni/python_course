#Generalize the above implementation of csv parser to support any delimiter and comments.
import sys
def openf():
	return open(sys.argv[1]).read()

def parse(f):
	y=f.split("\n")
	print [x.split(sys.argv[2]) for x in y]
 
parse(openf()) 
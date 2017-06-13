#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
import sys
def tailAndHead():
	x=open(sys.argv[1]).readlines()[:10]
	print "".join(x)

tailAndHead()
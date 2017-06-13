#Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
import sys
def grepfun():
	x=open(sys.argv[1]).readlines()
	for i in x:
		if sys.argv[2] in i:
			print i

grepfun()
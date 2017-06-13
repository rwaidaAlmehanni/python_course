#Write a program to print each line of a file in reverse order.
import sys
def reversLineContant():
	x=open(sys.argv[1]).readlines()
	for i in x:
		y=i.split()[::-1]
		print " ".join(y)

reversLineContant()
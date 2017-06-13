#Write a program reverse.py to print lines of a file in reverse order.
import sys
def reverse():
	print open(sys.argv[1]).readlines()[::-1]

reverse()


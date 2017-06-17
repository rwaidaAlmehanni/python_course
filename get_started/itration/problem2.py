#Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
import sys
def readlines40():
	print [line for line in open(sys.argv[1]).readlines() if len(line)>=40]

readlines40()

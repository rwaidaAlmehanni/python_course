#Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.
import sys
def mydoc():
	print sys.argv[1].__doc__
	# f={}
	# f[NAME]=sys.argv[1].NAME
	# f[FILE]=sys.argv[1].FILE
	# f[DESCRIPTION]=sys.argv[1].DESCRIPTION
	# f[FUNCTIONS]=sys.argv[1].FUNCTIONS
	# print f

mydoc()	
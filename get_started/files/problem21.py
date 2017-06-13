# Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
def warp():
	x=open(sys.argv[1]).readlines()
	for i in x:
		print i[:int(sys.argv[2])]

warp()

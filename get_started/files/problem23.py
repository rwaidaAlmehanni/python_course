#Write a program center_align.py to center align all lines in the given file
import sys
def center_align():
	length=[]
	x=open(sys.argv[1]).readlines()
	for i in x:
		length.append(len(i))
	m=max(length)
	for j in x:
		print j.center(m, ' ')
		
center_align()
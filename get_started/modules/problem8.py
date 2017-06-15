# Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.
import sys
def links():
	s=[]
	aindex=-1
	f=str(open(sys.argv[1]).read())
	arr=f.split()
	for i in arr:
		if i.index("herf"):
		    print i
		else:
			print "hello"
	# 		s.append(i[aindex:])
	# print s
	
links()	


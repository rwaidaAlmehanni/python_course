#Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.
import sys
def antihtml():
	s=""
	i=0
	f=str(open(sys.argv[1]).read())
	while i < len(f):
		if f[i] == "<" :
			x=f[i:].index(">")
			i+=x+1
		else:
			s+=f[i]
			i+=1
	print s
	
	

antihtml()
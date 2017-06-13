#The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
import sys
def wordwrap():
	x=open(sys.argv[1]).readlines()
	print x
	for i in x:
		if len(i)<sys.argv[2] :
			print i
		elif x[int(sys.argv[2])] == " " :
			print i[:int(sys.argv[2])]   
        else:
       	    print i[:int(sys.argv[2])+i[int(sys.argv[2]):].index(" ")]

wordwrap()       	

#What will be the output of the following program?
x=1
def f():
	y=x
	x=2
	return x+y

print x  #1
print f() #problem coz can't give value and assignmente again
print x	#1
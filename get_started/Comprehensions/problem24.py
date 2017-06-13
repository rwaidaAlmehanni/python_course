#Provide an implementation for zip function using list comprehensions.
def zip(a,b):
	print [(x,y) for x in a for y in b if a.index(x) == b.index(y)]

zip([1,2,3],["a","b","c"])
#Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.
def mapfunc(fn,array):
	print [fn(x) for x in array]

def square(x): return x * x

mapfunc(square, range(5))

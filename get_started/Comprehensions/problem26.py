# Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.
def even(x): return x %2 == 0 

def filterfun(fn,array):
	print [x for x in array if fn(x)]

filterfun(even, range(10))
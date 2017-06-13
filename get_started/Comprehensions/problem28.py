#Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
def enumerate(array):
	print [(array.index(y),y) for y in array]

enumerate(["a", "b", "c"])
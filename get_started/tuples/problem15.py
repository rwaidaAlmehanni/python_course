#Reimplement the unique function implemented in the earlier examples using sets
def unique(array):
	x=set([])
	for i in array:
		x.add(i)
	print x

unique([1,4,3,1,2])

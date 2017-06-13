#Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
def array(a,b):
	x=[]
	for i in range(b):
		x.append(None)
	print [x for y in range(int(a)) ]

array(2, 3)
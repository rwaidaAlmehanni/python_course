# Write a function valuesort to sort values of a dictionary based on the key.
def valuesort(f):
	arr=[]
	x=f.keys()
	x.sort()
	for i in x:
	  arr.append(f[i])
	print arr

valuesort({'x': 1, 'y': 2, 'a': 3})
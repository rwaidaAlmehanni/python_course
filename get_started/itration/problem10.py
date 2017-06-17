def izip(arr1,arr2):
	x=[]
	for i in range(len(arr1)):
		x.append((arr1[i],arr2[i]))
	print x

izip([1,2,3],["a","b","c"])	

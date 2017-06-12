def uniqueness(array,fn):
	x=[]
	array.sort(fn)
	for i in array:
		if i not in array[i+1:] :
			x.append(fn(i))
        print x

uniqueness(["python", "java", "Python", "Java"], key=lambda x: x.lower())        
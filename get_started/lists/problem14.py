#Problem 14: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
def uniqueness(array,fn):
	x=[]
	array.sort(fn)
	for i in array:
		if i not in array[i+1:] :
			x.append(fn(i))
        print x

uniqueness(["python", "java", "Python", "Java"], key=lambda x: x.lower())        
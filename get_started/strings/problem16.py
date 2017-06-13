# Write a function extsort to sort a list of files based on extension.
# in js
# function extsort(array){
# 	array.sort(function(a,b){ return a.slice(a.indexOf(".")) > b.slice(b.indexOf("."))})
# 	return array
# }
def sortxy(x,y):
    return x.slice(x.index("."))>y.slice(y.index(".")) 

def extsort(array):
	for i in array :
	    array.sort(sortxy(i,i+1))
	print array

extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

#Write a function dups to find all duplicates in the list.
# in js
# function dups(array){
#     var x=[];
# 	for(var i=0;i<array.length;i++){
# 	   if(array.slice(i+1).indexOf(array[i])!== -1){
	     
# 	       x.push(array[i])
	     
	   
# 	   }
# 	}
# 	return x
# }
def dups(array):
	x=[]
	for i in array :
		if i in array[i+1:] :
			if i not in x:
			   x.append(i)
	print x

dups([1,2,3,3,2,3])


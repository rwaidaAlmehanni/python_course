#Write a function cumulative_product to compute cumulative product of a list of numbers.
# in js
# function cumulative_sum(array){
# 	for (var i=array.length-1;i>=0;i--){
# 	  for(var j=0;j<i;j++){
#        array[i]+=array[j]
# 	  }
# 	}
# 	return array
# }
def cumulative_sum(array):
	z=0
	x=[]
	for i in array:
	    x.append(sum(array[0:i]))
	print x

cumulative_sum([4, 3, 2, 1])

# Write a function group(list, size) that take a list and splits into smaller lists of given size.
# in js
# # function group(array,n){
# #     var result=[],i=0;
# #  while (i<array.length){
#      result.push(array.slice(i,i+n));
# 	   i+=n
#      }
#    return result
# # }
def group(array,n):
	x=[]
	i=0
	while i < len(array):
		x.append(array[i:i+n])
		i+=n
        print x

group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)    

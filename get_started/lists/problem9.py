#Write a function cumulative_product to compute cumulative product of a list of numbers.
# in js:
# function cumulative_product(array){
# 	for(var i=array.length-1;i>=0;i--){
# 	   for(var j=0;j<i;j++){
# 	   array[i]*=array[j];
# 	   }
# 	}
# 	return array;
# }
def product(x):
	p=1;
	for i in x :
		p*=i
	return p
	
def cumulative_product(array):
    result=[]
    for i in array:
        result.append(product(array[0:i]))	
    print result


cumulative_product([1, 2, 3, 4])    	

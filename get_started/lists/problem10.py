#Write a function unique to find all the unique elements of a list.
# in js
# function unique(array){
# var x=[];
# for (var i=0;i<array.length;i++){
# 	if(array.indexOf(array[i])===array.lastIndexOf(array[i])){
#      x.push(array[i])
# 	}
# 	}
# 	return x;
# }
def unique(array):
	x=[]
	for i in array:
		if i not in array[i+1:] :
			x.append(i)
        print x

unique([1,2,3,2,3,7])
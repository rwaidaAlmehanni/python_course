#list or array on python simller to array on js it has dynamic length and can hold diffrent kind of data
 x = ["hello", "world"]
 x = [1, 2,3]
 y=[1,2,"x",[3,4]]

 #array with built_in function:
 len(y) # 4
 y[0] #1 on index 0 is the item 1
 y.append(8) #it will push to the end of the array this item y=[1,2,"x",[3,4],8]
 range(4) # [0,1,2,3] built_in function that create array by defult start from 0
 range(2,4) #[2,3,4] if it take 2 parameters it will create from the first one to the second on
 range(2,10,5) #[2,3,4,5,6] it will create from the first one to the second one as number given

 a=[1,2,3]
 b=[4,5,6]
 a+b #[1,2,3,4,5,6] will join the given lists
 a*2 #[2,4,6] will multiplay all the array elements with the given item
 a[-1] #3 it worke from revers index
 a[0:2] # [1,2] slice on python
 a[0:-1] # from the first element to the last one [1,2,3]
 
 x=[2,44,5,6,7,4,3]

 x[0] # 2 item in the first index
 x[1:3] # [44,5] from index 1 to 3 (3 not include)
 x[0:-1] # [2,33,5,6,7,4] all the element except the last on
 x[:2] # [2,44] all elemnts befor index 2
 x[3:] # [6,7,4,3] all elemnts from index 3 to the end
 x[:] # [2,44,5,6,7,4,3] all the elements
 x[0:4:2] #[2,5] from index 0 to index 4 every time increment the index+2(the theard elements)
 x[6:0:-1] # [3,4,7,6,5,44,2] will reverse the array
 x[::-1] # [3,4,7,6,5,44,2] will reverse the array the same will reverse the array from the end to the bigning
 2 in x # True in=include on js

 # for statement : for i in x will itrate from the first element the last one
 for i in x :
 print i # [2,44,5,6,7,4,3] i is the element on array not the index like js

 #zip is function that make the zip between 2 lists

 zip(["a","b"],[1,2]) #  [("a",1),("b",2)] 

 # itrate 2 list togither 
 for i,j in zip([1,2,3],[4,5]):
 print i,j #1 4
           #2 5
           #it will display the same numbers of elements depending on the shortest array
sum([1,2,3]) # 6 python has built_in function call sum
sum(["a","b"]) # "ab" join str





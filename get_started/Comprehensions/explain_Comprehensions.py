# it is a way to write operation inside [] in easy way like
# ex:
# a=range(10)
# a  [0,1,2,3,4,5,6,7,8,9]
# [x for x in a]  [0,1,2,3,4,5,6,7,8,9]
# [x+1 for x in a]  [1,2,3,4,5,6,7,8,9,10]
# [x*x for x in a]  [0,1,2,9,16,25,36,49,64,81]
# also we can use if:
# [x for x in a if x%2 == 0] [0,2,4,6,8]

# ex2:using with zip function
# a=[1,2,3]
# b=[10,20,30]
# [x+y for x,y in zip(a,b)]  [11,22,33]

# ex3:using with many for
# [(x,y) for x in range(2) for y in range(2) if(x+y)%2==0] [(0,0),(0,2),(1,1),(2,0)]

# >>> [(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0 and x != y]
# [(0, 2), (0, 4), (1, 3), (2, 0), (2, 4), (3, 1), (4, 0), (4, 2)]

# >>> [(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0]
# [(2, 0), (3, 1), (4, 0), (4, 2)]

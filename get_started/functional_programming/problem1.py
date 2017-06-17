#Implement a function product to multiply 2 numbers recursively using + and - operators only.
def product(n,x):
	if x==0:
	    return 0
	else:
		return n+product(n,x-1)
	 

r=product(2,3)
print r
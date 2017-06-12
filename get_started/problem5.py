#Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?
def product(array):
	x=array[0]
	for i in array:
	    x=x*i
        return x

def factorial(x):
    print product(range(1,x+1))	

factorial(4)

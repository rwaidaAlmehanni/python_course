class yrang:
	def __init__(self,n):
		self.i=0
		self.n=n

	def __iter__(self):
		return self

    def next(self):
    	if self.i<self.n :
    		i=self.i
    		self.i+=1
    		return i
    	else:
    		raise StopItration()

y=yrang(5)
y.next()
y.next()
y.next()


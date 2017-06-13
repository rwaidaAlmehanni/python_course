def triplets(n):
	print [(a,b,a+b) for a in range(1,n) for b in range(1,n) if a+b<n]


triplets(5)
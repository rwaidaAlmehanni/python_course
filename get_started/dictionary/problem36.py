def anagrams(arr):
	f={}
	for w in arr:
	  for l in w:
		f[l]=f.get(l, 0) + 1
    print f
	



anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
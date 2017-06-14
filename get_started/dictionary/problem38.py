#Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.
def invertdict(f):
    fr={}
    for i in f:
      fr[f[i]]=i
    print fr

invertdict({'x': 1, 'y': 2, 'z': 3})
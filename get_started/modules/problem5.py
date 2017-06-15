#Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.
import sys
import urllib

def readweb():
    f={}
    if str(sys.argv[1])[-1] != "/" :
  	    x=sys.argv[1].rfind("/")
  	    f[sys.argv[1][x+1:]]=str(urllib.urlopen(sys.argv[1]))
    else:
       f["index.html"]=str(urllib.urlopen(sys.argv[1]))
    print f

readweb()

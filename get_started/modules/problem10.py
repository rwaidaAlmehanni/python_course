# Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The program should print only the IP address and nothing else.
import urllib
import sys

def myIp():
    response = urllib.urlopen(sys.argv[1])
    print response.origin

myIp()    
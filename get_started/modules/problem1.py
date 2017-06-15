#Write a program to list all files in the given directory.
import sys
from os import listdir
def display():
    print listdir(sys.argv[1])

display()
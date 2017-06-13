# working with files in python:
# 1.open : used to open files
# f = open('foo.txt', 'r') # open a file in read mode
# f = open('foo.txt', 'w') # open a file in write mode
# f = open('foo.txt', 'a') # open a file in append mode
# *read:
# open('foo.txt').read() #to open file and read it
# open('foo.txt').readline() # will read one line from the file
# open('foo.txt').readlines() # will read all the file line by line (will return array of lines) 
 
# *write:
# >>> f = open('foo.txt', 'w') # it will open the file to write
# >>> f.write('a\nb\nc') # will write this lines in the file
# or
# f.writelines(['a\n', 'b\n', 'c\n'])
# >>> f.close() # should close the file after write inside it

# ex:
# function to count the numbers of char on file
# def charcount(filename):
#     return len(open(filename).read())

# function to count the numbers of words on file
# def wordcount(filename):
#     return len(open(filename).read().split())

# function to count the numbers of lines on file
# def linecount(filename):
#     return len(open(filename).readlines())





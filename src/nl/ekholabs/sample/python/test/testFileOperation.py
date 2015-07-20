'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports dictionaries module from com.irdeto.python.structure package.
'''
from com.irdeto.sample.python.io import fileOperation

'''
All calls in this module will use the file object wrapped by the module fileOperation.
'''

'''
Opens/Creates a file using the given name and default arguments.
'''
file = fileOperation.open_file('python_test.txt')

'''
Writes into the file.
'''
fileOperation.write_to_file(file, 'First line test\n')
fileOperation.write_to_file(file, 'Second line test\n')
fileOperation.write_to_file(file, 'Third line test\n')

'''
Flushes the file content and closes it.
'''
fileOperation.close_file(file)

'''
Open the already created file on Read mode.
'''
file = fileOperation.open_file('python_test.txt', 'r')

'''
Prints the first line from the file.
'''
print fileOperation.read_line(file)

'''
Reads the remaining lines from the file.
'''
lines = fileOperation.read_lines(file)

for l in lines:
    print l

'''
The file has been read till the end. To avoid errors trying to read again... o to reopen the file,
you can move the cursor to the beginning of the file instead.

First, get the current position of the cursor as a negative number
'''
pos = - file.tell()
'''
Then seek this position. It's important to know how the seek() function works and which parameters
can be passed on. The first parameters is the position (offset) you want to look for; the second
parameter is from which part of the file you want to measure (0 for beginning, 1 for current
position, and 2 for the end of the file).

In the code below, we have informed 1, which means from the current position - the offset. Since we
have read the whole file, we could have informed 2 instead. Both works fine in the scenario.
'''
file.seek(pos, 1)

'''
Now we can read the file from the beginning again.
'''
l1 = fileOperation.read_file_lines(file)

for l in l1:
    print l

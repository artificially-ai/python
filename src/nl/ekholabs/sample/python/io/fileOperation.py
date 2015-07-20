'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
This module shows how IO operations can be performed with files on Python. It simply open, write to
and read from a file.

To keep all the operation related to the file object in this module, we expect that you will pass
the file you got as argument to the methods you need to use. For now we are using modules, but once
we change to classes all the ideas of OOP will be used. So, encapsulating fields will be respected.

To sum up, you can simply open a file with Python using:
file open('file.txt', 'w'), meaning the name of the file and the mode you want to use it, respectively.
The current modes can be used:

    1. 'r' = read
    2. 'w' = write
    3. 'a' = append
    4. 'r+' = read and write

For non-text files (i.e. binary files) you have to use the following modes:

    1. 'rb' = read binary
    2. 'wb' = write binary
    3. 'r+b' = read and write binary 

We will not cover opening binary files here. But the functions you can use can be found below:

file = open('my_binary_file', 'r+b')
pos = file.tell() # returns the current position of the cursor within the file.
file.seek(pos, 10) # go to the 10th byte in the file
print file.read(file.tell()) # prints the content of the current position of the file.

DON'T FORGET TO HAVE A LOOK AT OBJECT SERIALIZATION WITH PYTHON.
HERE THEY CALL IT PICKLING AND UNPICKLING.

Examples:

    #Pickling
    file = open('my_file_object.txt', 'w')
    pickle.dump(object, file)
    file.close()
    
    #Unpickling
    file = open('my_file_object.txt', 'r')
    object = pickle.load(file)
    file.close()
'''

'''
Creates a file with the given name, using either default arguments for mode and path or the
arguments the developer passes as parameters.

The open/created file is returned to be used in later operations.
'''
def open_file(name, mode = 'a', path = 'C:/Users/wilder.rodrigues/python/'):
    try:
        file = open(path + name, mode)
        return file
    except IOError as error:
        raise error

'''
Writes a line into the file.
'''
def write_to_file(file, line):
    try:
        file.write(line)
    except IOError as error:
        raise error

'''
Reads a line from the file and moves the cursor to the next line.
'''
def read_line(file):
    try:
        return file.readline()
    except IOError as error:
        raise error

'''
Iterates over the file reading its lines and returns a list.
'''
def read_lines(file):
    try:
        list = []
        for line in file:
            list.append(line)
        return list
    except IOError as error:
        raise error

'''
Uses the readlines() function from the file object. It returns a list containing all the lines.
So, the function above doesn't make sense... it only shows how to iterate over a file object.
'''
def read_file_lines(file):
    try:
        return file.readlines()
    except IOError as error:
        raise error

'''
Flushes the file and closes it. It must be done in order to release resources. 
'''
def close_file(file):
    try:
        file.flush()
        file.close()
    except IOError as error:
        raise error

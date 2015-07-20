'''
Created on Sep 1, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
The first step into a new programming language: a simple Hello, Python World!
It also includes: function call; simple if statement; and string repetition.

Although, most important than that is to know how to add documentation to your code.
For Python, always use docstrings in your code. For example, this text has been created
with docstrings. If you want to add it to your code, just use \''' to open and \'''
to close. 
'''
hello = "Hello, Python World!"

'''
Stores the size of hello variable
'''
size = len(hello)

'''
Prints the content of hello onto the console
'''
print hello

'''
Prints the size of hello variable onto the console
'''
print size

'''
In Python, you can evaluate a boolean value from everything:

Examples...

my_1st_variable = None
my_2nd_variable = 'thing'

What returns True: if 1; if -1; if not ""; if 'thing'; if not None; if True; if not my_1st_variable; if my_2nd_variable
What returns False: if 0; if not 'thing'; if None; if not True; if ''; if my_1st_variable; if not my_2nd_variable

See the example below:
'''
flat_world = 1
if flat_world:
    print "Be careful not to fall off!"

'''
Now, assigning a negative value.
'''
flat_world = -10

if flat_world:
    print "Be careful not to fall off!"
else:
    print "You are safe."

if not flat_world:
    print "Be careful not to fall off!"
else:
    print "You are safe."

'''
Repeating 'test' 10 times.
'''
print 'test ' * 10

'''
Test slice statement.
'''
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print b[-1:]
print b[:-1]

def add_leading_zeros(number):
    if (len(number) == 1):
        return '000' + number
    if (len(number) == 2):
        return '00' + number
    if (len(number) == 3):
        return '0' + number
    else:
        return number

def convert_to_BCD(integer, leading_zeros = True):
    binary = ''
    for i in str(integer):
        part = ''
        d = int(i)
        while True:
            remain = d % 2
            d = d / 2
        
            part += str(remain)
        
            if not d:
                break
        
        part = part[::-1]
        if leading_zeros:
            binary += add_leading_zeros(part)
        else:
            binary += part
            
    return binary

#for i in range(1, 10):
#    print add_leading_zeros(convert_to_BCD(i))

print '-' * 30

print add_leading_zeros(convert_to_BCD(8442, False))

#print (2 << 1)

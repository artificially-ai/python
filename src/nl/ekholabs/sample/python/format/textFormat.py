'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports math module
'''
import math

'''
This module exposes functions used to format the text output. The same approaches can
be used when working with the terminal console or files.

Few ways of doing so will be exploited here.
'''

'''
This simple function just prints the squares and cubes of each number contained in the list.
With the constructor repr(object) we convert/print the value passed as parameter. In addition,
we called the function rjust(number) to specify that the text shall be aligned to the right for
max 2 characters (i.e. column width).

In the subsequent calls you can note that we use the same function to align the content. However,
we change the number of characters for 3 and 4, respectively. 
'''
def format_columns(list):
    for x in list:
        print repr(x).rjust(2), repr(x * x).rjust(3),
        # Note that we have a trailing comma on the previous line.
        print repr(x * x * x).rjust(4)

'''
This function does the same as the previous one. Although, it uses the function format() from the
module str. It's just easier than before to format the same list.

With format we don't need to use the trailing comma from the print. Also, we can simply inform the
index of the argument followed by the width of the column (e.g. {0:2d)

With the format() function you can use argument and keyword. So, you can use the keywords instead of
indexes. See the next function.

ATTENTION: On Python Tutorial it says that you can simply use:
    print 'Hello {}'.format('world')

IT'S NOT TRUE! It doesn't compile and gives the following error:
    ValueError: zero length field name in format
    
The right way to do that is:
    print 'Hello {0}'.format('world')
'''
def format_columns_2(list):
    for x in list:
        print '{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x)

'''
This function keeps doing the same thing as the previous two, but now we are using keywords in the
format() function.

ATTENTION: On Python Tutorial it says that you can simply use:
    print 'Hello {}'.format('world')

IT'S NOT TRUE! It doesn't compile and gives the following error:
    ValueError: zero length field name in format
    
The right way to do that is:
    print 'Hello {0}'.format('world')
'''
def format_columns_3(list):
    for x in list:
        print '{source:2d} {square:3d} {cube:4d}'.format(source = x, square = x * x, cube = x * x * x)

'''
This function, using an already used approach, prints a message to the output. The idea behind here is
just to introduce the math module and show how to inform if the formatter will use either str or repr.

To inform the type of formatter enter !s or !r for str or repr, respectively (default is !s). See the
other examples.

ATTENTION: On Python Tutorial it says that you can simply use:
    print 'Hello {}'.format('world')

IT'S NOT TRUE! It doesn't compile and gives the following error:
    ValueError: zero length field name in format
    
The right way to do that is:
    print 'Hello {0}'.format('world')
'''
def format_pi():
    print 'The value of PI is approximately {0}'.format(math.pi)

'''
Notice that with !r we can print slightly more decimals than with !s. 

ATTENTION: On Python Tutorial it says that you can simply use:
    print 'Hello {}'.format('world')

IT'S NOT TRUE! It doesn't compile and gives the following error:
    ValueError: zero length field name in format
    
The right way to do that is:
    print 'Hello {0}'.format('world')
'''
def format_pi_2():
    print 'The value of PI is approximately {0!r}'.format(math.pi)

'''
This function does almost the same as the previous ones, except that here we inform the number
of decimals and the format to be used.

ATTENTION: On Python Tutorial it says that you can simply use:
    print 'Hello {}'.format('world')

IT'S NOT TRUE! It doesn't compile and gives the following error:
    ValueError: zero length field name in format
    
The right way to do that is:
    print 'Hello {0}'.format('world')
'''
def format_pi_3():
    print 'The value of PI is approximately {0:.2f}'.format(math.pi)

'''
This function does almost the same as the previous ones, except that here we use keywords
instead of arguments.

ATTENTION: On Python Tutorial it says that you can simply use:
    print 'Hello {}'.format('world')

IT'S NOT TRUE! It doesn't compile and gives the following error:
    ValueError: zero length field name in format
    
The right way to do that is:
    print 'Hello {0}'.format('world')
'''
def format_pi_4():
    print 'The value of PI is approximately {pi:.3f}'.format(pi = math.pi)

'''
Created on Sep 6, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Dictionaries are very helpful and powerful data structures. A dictionary could be compared
with a Java HashMap, where you can have a key:value pair. So, that said, different from sequences
a dictionary is formed of an unordered set of key:value pairs.

As keys you can use almost everything, even tuples. However, they shall contain only strings.
Mutable objects cannot be used as keys of a dictionary.

This module will introduce the Dictionaries and show how to perform basic operations on them.
'''

'''
Given 2 parameters, where the second one is a dictionary, print their values and iterate
over the keys of the dictionary.

It's important to notice that the dictionary was sent as a literal. So, in order to use the
keys() function, we need to call the dict() constructor.

Also, the way we are iterating over the dictionary here is not the best one. In the second
function we shall show another way to iterate over it. 
'''
def coordinates_dict(file_name, coordinates):

    print 'file name', file_name
    
    '''
    Constructs a proper Dictionary based on the literal that was sent.
    '''
    coordinates_dict = dict(coordinates)
    keys = coordinates_dict.keys()
    for x in keys:
        print x, coordinates_dict[x]

'''
Prints out the key:value pair contained into the Dictionary. However, at this time it uses
the iteritems() function from the Dictionary.

In addition, at that time we are sending a proper Dictionary. Thus, no need to call the dict()
constructor.
'''
def coordinates_dict_2(file_name, coordinates):
    
    print 'file name', file_name
    
    for k, v in coordinates.iteritems():
        print k, v

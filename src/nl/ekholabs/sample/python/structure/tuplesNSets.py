'''
Created on Sep 6, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
This module has functions to perform operations on Tuples and Sets. In addition, the del
statement is shown, explaining how to remove items from a list.
'''

'''
Prints (could store) user information existing in the profile passed as parameter.
The profile has been built as a Tuple, so we expect it to have different types. For examples,
if a profiles consists of the correspondence address of the user, it will contain strings,
numbers, and perhaps even nested Tuples.

At this point is important not to try to associate the values of a Tuple to already defined and
instantiated variables.

As an example, a profile could be:

profile = 'Wilder', 'Rodrigues', '01/10/1979', '3544VS', 'Eerste Westerparklaan', 49
'''
def store_user_info(profile):
    print profile

'''
Prints each value of the Tuple to the console. However, this method expects nested Tuples. Thus, the
outer for loop iterates over the first dimension of the Nested Tuples; the inner for loop iterates
over the elements of the second dimension. As result, we have the values printed to the console.

As an example, a multi-dimensional Tuble could be:

profiles = profile, ('Erika', 'Nattrodt', '03/09/1979', '3544VS', 'Eerste Westerparklaan', 49)

Parentheses SHALL be informed.
'''
def print_user_info(profiles):
    for i in range(len(profiles)):
        for j in range(len(profiles[i])):
            print profiles[i][j]
'''
This function either removes of add the given X value to the given data Set.
In order to perform this operation, this function checks if the x is already in the set. If so,
it removes this value with the operation:

data = data - xx

Notice that xx is created at the beginning of the function with the value of x. The operation
data - xx returns a new Set with all the elements of data that are not in x. So, it's easy to
remove the x value.

In the case the value of x is not in the data Set (else statement), the function will add the x value
to the data Set and print it out. To be able to do so, the following operation is performed.

data = data ^ xx

THis operation returns a new Set with the content of data (that is not contained in xx) and the
content of xx. Thus, a complete Set.

Other operations that can be performed with Sets are:

data = data | xx # Returns a set with the content either in data or xx
data = data & xx # Returns a set with the content in both data and xx

In our case, we could use:

data = data ^ xx # within the if body

data = data | xx # within the else body
'''
def inspect_set(x, data):
    xx = set(x)
    if x in data:
        data = data - xx
        print data
    else:
        data = data ^ xx
        print data

'''
Removes the element in the given index of the given list. In the case the element exceeds the boundary
of the list, an error is raised.

In this function, the del statement is used. To see how to use the del statement with slices, refer to
tuplesNSetsCalls.py module.
'''
def remove_element(index, list):
    if index >= len(list):
        raise IndexError('The index informed is greater than the size of the current list.')
    del list[index]

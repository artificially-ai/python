'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Import functions3rd module from com.irdeto.python.module package.
'''
from com.irdeto.sample.python.module import functions3rd

'''
This module contains calls to the functions within the functions3rd.py module. It's using
couple of Functional Programming tools to create lists based on the evaluation of the function
used by the tool. See examples below.
'''

'''
Filters the values of the given range in order to extract prime numbers. For each value within
the range, the evaluation will return either true or false. In the case the return is True, the
value will be added to the list. Once the whole sequence (range(), in that case), has been observed,
the final list is returned.

If the sequence passed as parameters is a string or tuple, the same type will be returned; otherwise,
a list will be always returned.
'''
print filter(functions3rd.primes, range(2, 25))

'''
Returns a list containing the cube calculation of each value in the sequence given as parameter.
'''
print map(functions3rd.cube, range(1, 15))

'''
This one is silly and is used only to show the map() function using 2 sequences.
It calls the functions3rd.year_of_birth function, which expects the age and current year in order to
find the year of birth.

Since we need 2 sequences, we have to make sure that they have the same size. So, we cannot send
the year list containing only the current year. For each entry in the age list, we need to repeat the year.

That's the silly part and it had to be explained. You can find a better example using Lists Conprehension.
'''
year = [2010, 2010]
age = [30, 50]

print map(functions3rd.year_of_birth, age, year)

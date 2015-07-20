'''
Created on Sep 3, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
This module contains simple functions. However, they are being used by Functional Programming tools
in order to offer a better way to create lists based in sequences and logical operations.

Please, refer to functionCalls3rd.py module in order to see how those functions are being used.
'''

'''
Returns true if the given parameters if a prime number.
'''
def primes(x):
    return x == 2 or x % 2 != 0 and x % 3 != 0

'''
Returns the cube of the given number X.
'''
def cube(x):
    return x * x * x

'''
Returns the year of birth based on the age and current_year parameters.
'''
def year_of_birth(age, current_year):
    return current_year - age

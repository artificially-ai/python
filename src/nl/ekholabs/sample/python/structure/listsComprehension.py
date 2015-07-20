'''
Created on Sep 6, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
This module contains couple of functions to show how we can work with Lists Comprehensions.
Those lists provide a way to create lists without abusing the use of map() and filter functions.
In addition, more logic may be entered in the function responsible by creating the list.
'''

'''
Returns a list with the prime numbers contained in the list passed as parameter.
Notice the used of [] to wrap the for loop and also the if statement nested within the loop.
The returning list will be created according to the evaluation of the if statement.
'''
def extract_primes(vec):
    return [x for x in vec if x == 2 or x % 2 != 0 and x % 3 != 0]

'''
Returns a list containing the year of birth according to the list of ages and current year
passed as parameters. Notice that in this function we don't need to inform a sequence with the
current year repeated over.

Another important point is the use of arithmetic expressions to generate the values for the
returning list.
'''
def year_of_birth(vec_ages, current_year):
    return [current_year - vec_ages[i] for i in range(len(vec_ages))]

'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports listsComprehension from com.irdeto.python.structure package.
'''
from com.irdeto.sample.python.structure import listsComprehension

'''
Calls a function from the listsComprehension module in order to extract the prime number
within the range 2 to 100 (exclusive).
'''
vec = range(2, 100)
list = listsComprehension.extract_primes(vec)
print list

'''
Calls a function from the listsComprehension module in order to calculate the year of
birth of a given list of ages. The function also takes as parameter the current year.
'''
vec_age = [30, 25, 55, 21, 8, 12, 68, 113]
year = 2010
list2 = listsComprehension.year_of_birth(vec_age, year)
print list2

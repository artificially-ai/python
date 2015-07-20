'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Fibonacci series in Python: the sum of two elements defines the next

This examples contains calls to Python functions and a function of our own.
The import statement, in the first line, imports the module fibonacci into
the variable Fibonacci.

To iterate over the array containing the Fibonacci series, we use a
for loop along with the range() function.
'''

'''
Imports fibonacci module from com.irdeto.python.module package.
'''
from com.irdeto.sample.python.module import fibonacci

'''
It's simple and readable. The for loop will iterate over the result according
to what is specified by the range() function.

This function will store a value, starting from 0, into the variable i. The last
value for i is equals to length of the result (exclusive).  
'''
fib_result = fibonacci.fib(1000)

for i in range(len(fib_result)):
    print fib_result[i],

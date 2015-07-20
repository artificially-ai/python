'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
This module contains only one functions, used to calculate and return
a Fibonacci series up to a given N parameter. 
'''

'''
Caculates and return a Fibonacci series up to N, a given parameter.
Notice the use of the Multiple Assignment within the fib() function.
'''
def fib(n):
    print ' Returns a Fobinacci series up to ', n
    
    result = []
    
    '''
    Nice feature from Python: multiple assignment
    '''
    a, b = 0, 1
    while a < n:
        result.append(a)
        '''
        Multiple assignment used once more.
        '''
        a, b = b, a + b
    return result

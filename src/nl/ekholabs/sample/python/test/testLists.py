'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports lists module from com.irdeto.python.structure package.
'''
from com.irdeto.sample.python.structure import lists

'''
This module is used to perform few calls to functions within the lists module.
'''

'''
Tests few operations with lists. See the content of the function for clarification.
'''
fruits = ['Apple', 'Kiwi', 'Mango', 'Grapes']
lists.using_list('Cherry', fruits)

'''
Tests a stack behavior (last in, first out).
'''
numbers = [1, 15, 60, 3, 5, 8, 25, 61, 70]
lists.lifo(50, numbers)

'''
Tests a queue behavior. However, within the function, a bit of priority assuming that an older
person arrives at the queue.
'''
people = ['Johan', 'Tom', 'Raj', 'Berry']
lists.fifo('Silvia', people)

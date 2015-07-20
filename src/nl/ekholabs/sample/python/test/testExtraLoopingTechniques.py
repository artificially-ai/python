'''
Created on Sep 7, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Looping techniques over sequences.
1st: enumerating sequences
'''
seq = ['tic', 'tac', 'toe']
for i, v in enumerate(seq):
    print i, v

'''
2dn: looping over two paired sequences with zip(). Notice the use of format() function.
'''
q = ['name', 'quest', 'favorite color']
a = ['Lancelot', 'the holy grail', ', blue']
for q1, a1 in zip(q, a):
    print 'What is your {0}? It is {1}.'.format(q1, a1)

'''
3rd: looping over the sequence in reverse order.
'''
for i in reversed(range(1, 10, 2)):
    print i

'''
4th: looping over a sorted sequence
'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f

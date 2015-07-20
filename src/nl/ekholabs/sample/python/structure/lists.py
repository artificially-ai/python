'''
Created on Sep 3, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
This file comprises a few functions used to manipulate lists, queues and stacks. It shows
the behavior of those data structures.
'''

'''
Imports the deque object from the collections module.
'''
from collections import deque

'''
This function only shows how to use few methods from a list
(e.g. append, index, insert, reverse, sort, etc). It is useful to get in touch
with the possibilities when using a list. 
'''
def using_list(x, list):
    print 'list size', len(list)
    
    '''
    Adds the given object to the end of the list.
    '''
    list.append(x)
    print list.index(x)
    print 'list size', len(list)
    
    '''
    Adds the given objects (in that case, the 'x' concatenated with itself)
    to the given position (index) in the list.
    '''
    list.insert(0, x + x)
    print list
    
    list.reverse()
    print list
    
    '''
    Sorts the list elements.
    '''    
    list.sort()
    print list
    
    '''
    Remove and returns the last element of the list. You can also
    inform an index to be used by this function.
    e.g.: list.pop(0) will remove and return the first element.
    '''
    print list.pop()
    
    print list

'''
This functions shows how to use a list as a stack (LIFO). 
'''
def lifo(x, stack):
    
    print stack
    
    '''
    Adds the given object to the stack (goes to the top of it)
    '''
    stack.append(x)
    print stack
    
    '''
    Adds more objects to the top of the stack.
    '''
    stack.append(x + 2)
    stack.append(x * 2)
    print stack
    
    '''
    Adds more objects to the top of the stack.
    '''
    for i in range(50, 100, 30):
        stack.append(i)
    print stack
    
    '''
    This loop iterates over the stack and removes its elements, from top to bottom.
    The function pop(), as told before, removes and return the last (top) element
    of the stack.
    '''
    for i in range(0, len(stack)):
        stack.pop()
    print stack

'''
This function uses a list to implement a queue (FIFO)
'''
def fifo(x, q):
    '''
    Creates a queue using the given list.
    '''
    queue = deque(q)
    print queue
    
    '''
    The object given as parameters arrives into the queue. It goes to the end
    of the queue.
    '''
    queue.append(x)
    print queue
    
    '''
    Grandmother is 60 years old. She has priority and goes to the beginning
    of the queue. Use queue.appendleft() function for this.
    '''
    queue.appendleft('Grandmother')
    
    '''
    Goes to the end of the queue.
    '''
    queue.append('Robert')
    print queue
    
    '''
    This while loop iterates over the queue and removes its elements.
    The popleft() function removes the elements in the front of the queue.
    '''
    while len(queue) != 0:
        print queue.popleft()
    
    print queue

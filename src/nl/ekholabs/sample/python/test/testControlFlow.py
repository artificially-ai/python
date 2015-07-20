'''
Created on Sep 1, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
The snippet codes here are used to explain a bit about Control Flow on Python
and couple of functions basically used in these structures.

To make easier and a bit more dynamic, the program reads the user input from the console.  
'''

'''
The raw_input() function reads the user input and stores into an integer.
'''
x = int(raw_input("Please enter an integer: "))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

'''
That's the closest thing we have to an array in Java. Create the array than print
it out to the console.
'''
a = ['cat', 'window', 'defenestrate']
print a

'''
Iterate over the values of the array a. However, notice that we are not
using the indexes for iteration, but the values contained in a.
The print statement concatenates the value (in b) with the length of the value.
'''
for b in a:
    print b, len(b)

'''
In order to copy an array during the iteration, you have to provide a slice of it.
The snippet below copies the array a, iterates over it and insert a value at the
beginning of the array (in case it corresponds to the if statement)

A slice copy can be taken also informing index to start and finish:

copy_of_a = a[10:len(a)]

The snippet above would copy from position 10 till the length of a (exclusive). 
'''
for b in a[:]:
    if len(b) > 6:
        a.insert(0, b)

print a

'''
Couple of tests with range() function. The first print statement will print out
the range from 0 to 10 (exclusive). So, on the console output, you can see the sequence
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

The second print statement will print out the range from 0 to 100 (exclusive), but now
it uses a third parameters responsible for the step increment. In the case, we will print
from 0 to 100 with steps of 10. So, the output will be:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

It's goes only till 90 because 100 (the length) is exclusive.
'''
print range(0, 10)
print range(0, 100, 10)

'''
Using range to iterate over an array. In that case, since we wnat the whole array,
we don't need to inform the start index in the range() call. The for loop shall
iterate from 0 to len(aa) - exclusive.
'''
aa = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(aa)):
    print i, aa[i]

'''
This snippet just tests if a given number is prime. Here we use range() to
iterate over a anonymous array created within the loop. SO, from range(2, x)
- x was entered via the user input - it checks if the number is not a prime
(by performing n % xx == 0) in the if statement. Once it falls there, the inner
loop will stop and the index in the outer loop will be incremented.

Notice that the for statement has an else clause, which will be executed
once the inner loop fails to find a factor.
'''
for n in range(2, x):
    for xx in range(2, n):
        if n % xx == 0:
            print n, 'equals', xx, '*', n/xx
            break
    else:
        '''
        Loop fell through without finding a factor. Now it prints the number
        concatenated with a proper message.
        '''
        print n, 'is a prime number.'

'''
Every function on Python has a return value. However, if the return statement is
not explicit, the function returns None. If None is printed out, the only thing you can
see is the string None. See on the snippet below:
'''
print None

'''
The 'pass' statement is used only to indicate that a statement is required syntactically,
but no action is required. In the example below, the pass is used to validate the while
statement. If nothing is informed within the while body, it won't compile. For that, we
need at least a pass statement.

Another use for 'pass' is to inform that a method still needs to be finished. So, the pass only
works as an indication. Is always useful to add some documentation with a method with a pass
statement within.
'''
while 1:
    '''
    while 1 has the same evaluation as while -1 or while not "" or while not None or while True: the evaluation is TRUE
    On the other hand, while 0 has the same evaluation as while not 'thing' or while None or while not True: the evaluation is False
    
    Doesn't do anything... just exit it by pressing CTRL+C
    '''
    pass

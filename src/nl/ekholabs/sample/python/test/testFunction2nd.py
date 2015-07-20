'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports functions2nd module from com.irdeto.python.module package.
'''
from com.irdeto.sample.python.module import functions2nd

'''
Simple test, just calling a function with required and optional parameters.
'''
functions2nd.print_message('Logan', '100km')

'''
Using anonymous functions, created through the Lambda form, to increment the number that was
initially given to the Lambda form. Once the anonymous function is created, the value informed
will be kept in memory. So, the increment method only sums the new value with the first one.
Consecutive calls won't keep incrementing. So, the calls below will generate the following output:

print i(2) # 12
print i(5) # 15

But you are free to create your Lambda forms... please check the content of chat() function.  
'''
i = functions2nd.increment(10)
print i(2)
print i(5)

'''
This one is a bit more complex. However, it doesn't mean that working with Lambda form is difficult.
Now you understand a bit about Lambda forms, have a look at source code of the function chat.
'''
hello = functions2nd.chat('Jeroen')
print hello('Hello ', '.')
print hello('How are you doing, ', '?')

'''
Calling a function that doesn't do anything. It has a definition and a pass statement in order to
inform that the method is under implementation. More about pass statement, please check the
comments within the todo_function.
'''
functions2nd.todo_function()

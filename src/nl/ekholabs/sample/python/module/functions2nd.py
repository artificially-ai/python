'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
THis module exhibits the usage parameters lambda function and the pass statement.
Two of them you have already seen in other modules, but it's important to spread the
use of simple functions just to keep them in mind. 
'''

'''
This function simply prints out a message using 2 parameters. As you have seen begore, the
name is required because it doesn't have a default value; by the other hand, since it has
a value define, the parameter distance is optional.

The developer may decide to change the distance parameter in order to pass a different
parameter, or even type. Since Pytonh is not a strongly typed language, you could do something
like that:

print_message('Johan', 100)

However, 100 doesn't make sence in the output, which would be:

Johan is not allowed to run 100.

So, better to have a string:

print_message('Johan', '100km')

And you can figure out what would be the result.
'''
def print_message(name, distance = 'hundred metres'):
    print name + ' is not allowed to run', distance

'''
This function uses the Lambda form to create an anonymous function used to increment a given N value.
The Lambda form saves in memory (e.g. during execution time of the interpreter) the first value
given to N. Any consecutive call to the anonymous function will execute the arithmetic operation
defined by lambda. For example:

count = increment(10)
print count(2) #prints 12
print count(4) #prints 14   
'''
def increment(n):
    return lambda x: x + n

'''
Another function using Lambda form to print messages. This one is a bit more complex than the
first one, having 2 parameters specified by the lambda form.

AN example of how it works can be seen below:

sentence = chat('Kevin')
print sentence('Hello ', '.')
print sentence('How are you doing, ', '?')
print sentence('Where do you live, ', '?')

The output would be:

Hello Kevin.
How are you doing, Kevin?
Where do you live, Kevin?

Pretty handy. ;)
'''
def chat(x):
    return lambda text, ponctuation: text + x + ponctuation

'''
As it has been explained before, the pass statement is used only to syntactically allow a
function without body to compile.

The function below doesn't do anything, but it doesn't cause errors either.
'''
def todo_function():
    """Function under construction. Please
    come later, when some code would be provided."""
    pass

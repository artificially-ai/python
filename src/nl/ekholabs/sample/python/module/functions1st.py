'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports the upper() function from the string module.
'''
from string import upper

'''
This module exhibits the use of Control Flow statements, parameterization, keywords
and the first look into raising errors.
'''

'''
This function has a simple job of asking the user to enter his gender and extracting
the entered information from the console input. From the 4 parameters, 2 are required:
prompt and name. The other 2 have received default values within the declaration.
If the developer wants to change those values, it's just a matter of passing new ones
to the function.

As you have seen in other example, raw_input() is responsible for reading the input.
The upper() function, imported from string module, changes the case of the entered attribute
to have it easily tested by the if statement.

The if statement consists of a nested Else If (elif) and is finished with an else.

If by any chance the number of retries is reached, an error shall be raised with the
message passed as parameter. 
'''
def ask_gender(prompt, name, retries = 5, error_message = 'Please, enter your gender.'):
    while True:
        gender = raw_input(prompt)
        if upper(gender) in ('M', 'MALE'):
            return 'Welcome, Mr. ' + name
        elif upper(gender) in ('F', 'FEMALE'):
            return 'Welcome, Mrs. ' + name
        else:
            retries = retries - 1
        if (retries < 0):
            '''
            Raise an IOError after x number of retries. 
            '''
            raise IOError(error_message)

'''
Prints a full correspondence address. However, the printing order is not standardized,
only sorted.

This function introduces the use of arguments and keywords (second and third parameters).
However, those parameters are optional. An example of how to call this function can be found
below:

print_address('Ms.', 'Angelina', 'Jolie', city = 'somewhere', postcode = '123', country = 'USA')

From the second parameter you can identify the arguments (i.e. Angelina, Jolie). After that, you can
see clearly the keywords being used.
'''
def print_address(title, *name, **address):
    print title
    for n in name:
        print n,
    '''
    Extracts the keys from the keywords
    '''
    keys = address.keys()
    '''
    Sort the keys.
    '''
    keys.sort()
    '''
    Iterate over the sorted keys.
    '''
    for k in keys:
        print address[k]

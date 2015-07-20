'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports tuplesNSets from com.irdeto.python.structure package.
'''
from com.irdeto.sample.python.structure import tuplesNSets

'''
Using Tuples to create a profile.
'''
profile = 'Robert', 'Poulsen', '01/10/1979', '123AB', 'After the Corner Street', 49
tuplesNSets.store_user_info(profile)

'''
Multi-dimensional (or Nested) Tuples to create a nested profiles.
'''
profiles = profile, ('Helen', 'Bohan', '03/09/1979', '145CB', 'Around the Corner Street', 49)
tuplesNSets.store_user_info(profiles)

tuplesNSets.print_user_info(profiles)

'''
The marvelous unpacking sequence. With this kind of assignment, the developer can unpack
the content of a tuple within keywords.
'''
name, surname, birth, postcode, address, number = profile
print name, surname, birth, postcode, address, number

'''
Let's now demonstrate some set operations. Starting with a list that will be used to create a Set.
You can also create a Set from a string
s = set('abcd')

print s will result in ['a','b','c','d']

Remember: a string is an array of characters.
'''
b = ['x', 'y', 'z']
data = set(b)

'''
Simple call to a function that will realise an operation on the given Set.
'''
tuplesNSets.inspect_set('w', data)

'''
Creates a new list in order to use with del statement.
'''
x = [1, 2, 3, 4, 5, 6]
print x

tuplesNSets.remove_element(0, x)
print x

'''
Using the del statement to clear the list. Since you can inform slices, you are able to stuff like that:

del x[2:5]
'''
del x[:]

'''
After clearing the list, try to remove the element on index 0. It shall fail and raise an error
because the list is empty.
'''
tuplesNSets.remove_element(0, x)

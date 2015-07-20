'''
Created on Sep 7, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports dictionaries module from com.irdeto.python.structure package.
'''
from com.irdeto.sample.python.structure import dictionaries

'''
Creates a dictionary with a literal and passes it through the coordinates_dict() function
'''
coordinates = {'lat': 52.36, 'long': 4.72}
dictionaries.coordinates_dict('123456', coordinates)

'''
Creates a dictionary using the dict() constructor. Notice that since we are using simple strings as key,
we don't have to specify pairs as keyword arguments.
'''
coordinates_dict = dict(lat = 52.37, long = 4.70)
dictionaries.coordinates_dict_2('654789', coordinates_dict)

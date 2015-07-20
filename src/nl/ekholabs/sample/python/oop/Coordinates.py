'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
PBean (what I call Python Bean) Coordinates.
'''
class Coordinates():
    
    def __init__(self, lat, long):
        '''
        Class constructor.
        '''
        self.lat = lat
        self.long = long
    
    def __str__(self):
        '''
        Overrides the __str__ function in order to return a formatted string.
        '''
        return '[latitude: {0}, longitude: {1}]'.format(self.lat, self.long)

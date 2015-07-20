'''
Created on Sep 9, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

class GeocodeError(Exception):
    '''
    Exception used to inform about errors occurred during geocode attempts.
    '''
    
    def __init__(self, coordinates, message):
        '''
        Class constructor taking as parameters the coordinates used for geocode and the error message.
        '''
        self.coordinates = coordinates
        self.message = message
    
    def __str__(self):
        '''
        Overriding the __str__ function to have a proper error message printed to the console.
        '''
        return 'Exception occurred: {0}; {1}; {2}.'.format(self.coordinates.lat, self.coordinates.long, self.message)

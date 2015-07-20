'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''
from com.irdeto.sample.python.logging import BaseLogger
from com.irdeto.sample.python.exception.GeocodeError import GeocodeError
from webbrowser import Error

import webbrowser

class GeocodeService(BaseLogger.BaseLogger):
    '''
    This class was created with the intention to use your latitude and longitude to perform a geocode call
    against Google Maps services. However, since the Google Maps blocks access from stand-alone application,
    it's not possible to retrieve the information.
    
    In order to have some use for this class, the Exception handling has been added to test Python's capabilities.
    '''
    
    __GOOGLE_MAPS_QUERY_URL__ = 'http://maps.google.nl/maps?q={0},{1}'
    __GOOGLE_MAPS_GEOCODE__ = 'http://maps.google.nl{0}'
    
    '''
    Default constructor. This is a stateless services, so no need to create attributes. Use pass statement to be able
    to compile an empty constructor.
    '''
    def __init__(self):
        BaseLogger.BaseLogger.__init__(self)
    
    def geocode(self, coordinates):
        '''
        Tries to retrieve you geo location for the given coordinates.
        The first argument SHALL be self. If you don't inform it the class won't compile. 
        '''
        
        url_to_open = self.__GOOGLE_MAPS_QUERY_URL__.format(coordinates.lat, coordinates.long)
        self.info('Try to copy/paste this {0} into your browser.'.format(url_to_open))
        
        try:
            '''
            @deprecated:  Tries to connect to Google Maps URL using the given coordinates.
            It shall throw an URLError, which will be caught and handled.
            
            Now I'm using webbrowser.get('windows-default') just to open Google Maps with the given
            variable. It's better than returning an error from Google.
            '''
            browser = webbrowser.get('windows-default')
            return browser.open(url_to_open, 2, True)
            #for line in page:
            #    if '/maps?q=&' in line:
            #        return line
        except Error as error:
            '''
            Raise a GeocodeError to the caller of this function.
            '''
            self.error(error)
            raise GeocodeError(coordinates, error)

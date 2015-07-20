'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''
from com.irdeto.sample.python.oop.Coordinates import Coordinates
from com.irdeto.sample.python.oop.GeocodeService import GeocodeService
from com.irdeto.sample.python.exception.GeocodeError import GeocodeError
from com.irdeto.sample.python.logging.BaseLogger import BaseLogger

log = BaseLogger()

'''
Creates a new instance of Coordinates class with the given latitude and longitude.
'''
coordinates = Coordinates(52.291499, 4.699767)

'''
Creates a new instance of the GeocodeService class. 
'''
geocode = GeocodeService()

'''
Performs a geocode call to the GeocodeService service. It shall fail because Google blocks calls
from stand-alone applications. However, we handle the exception within the except block.
'''
try:
    print geocode.geocode(coordinates)
except GeocodeError as error:
    log.error(error)

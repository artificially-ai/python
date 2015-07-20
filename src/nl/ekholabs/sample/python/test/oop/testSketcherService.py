'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''
from com.irdeto.sample.python.oop.Coordinates import Coordinates
from com.irdeto.sample.python.oop.SketcherService import SketcherService
from com.irdeto.sample.python.logging.BaseLogger import BaseLogger

log = BaseLogger()

'''
Creates a new instance of Coordinates class with the given latitude and longitude.
'''
coordinates = Coordinates(52.291499, 4.699767)

'''
Creates a new instance of SketcherServices in order to store coordinates.
'''
sketcher = SketcherService()

'''
The file name attribute is option for store_coordinates function. If not given, a new unique file
name will be generated and returned in order to be reused for later appending operations.
'''
file_name = None
try:
    file_name = sketcher.store_coordinates(coordinates)
except IOError as error:
    log.error(error)

'''
Change coordinates and stora in an already existing file.
'''
coordinates.lat, coordinates.long = 52.366769, 4.896469
try:
    if file_name:
        sketcher.store_coordinates(coordinates, file_name)
except IOError as error:
    log.error(error)

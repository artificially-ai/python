'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''
from com.irdeto.sample.python.logging import BaseLogger
from com.irdeto.sample.python.io import fileOperation
from uuid import uuid1

class SketcherService(BaseLogger.BaseLogger):
    '''
    Service used to store coordinates into the file system.
    '''
    
    def __init__(self):
        '''
        Class constructor.
        Notice that it calls the constructor of the base class.
        '''
        BaseLogger.BaseLogger.__init__(self)
            
    def store_coordinates(self, coordinates, file_name = uuid1().__str__()):
        '''
        Stores the coordinates object into a file. If the file name is not informed, a new unique name will be
        generated. Once the store operation is done, this function returns the file name used for future
        actions.
        
        @param coordinates: to be stored.
        @param file_name: has a default value when not informed. It uses uuid1() function to generate the file name.
        '''
        file = None
        try:
            file = fileOperation.open_file(file_name)
            fileOperation.write_to_file(file, coordinates.__str__() + '\n')
        except IOError as error:
            '''
            Logs errors occurred during store operation.
            '''
            self.error(error)
            raise error
        else:
            '''
            If nothing wrong occurred, log info.
            This statement is only executed if there is no return statement within the try block.
            '''
            self.info('Coordinates stored successfully.')
            return file_name
        finally:
            '''
            Closes the stream and flushes the file.
            '''
            try:
                if file:
                    fileOperation.close_file(file)
            except IOError as error:
                self.error(error)

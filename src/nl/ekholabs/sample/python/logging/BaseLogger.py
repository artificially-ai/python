'''
Created on Sep 9, 2010

@author: wilder.rodrigues
'''
from logging import handlers
from datetime import datetime
import logging

class BaseLogger():
    '''
    This class may be extended by any other class in order to introduce logging mechanism.
    You can either used this class or have a logging of your own into your classes. However,
    it would replicate code everywhere.
    '''
    
    LOG_FILENAME = 'C:/Users/wilder.rodrigues/log/sketcher_log_file.log'
    
    def __init__(self):
        '''    
        Class constructor.
        It initialises the log and handler attributes.
        '''
        self.log = logging.getLogger('BaseLogger')
        self.log.setLevel(logging.INFO)
        self.handler = handlers.RotatingFileHandler(self.LOG_FILENAME, maxBytes = 1024*1024, backupCount = 5)
        self.log.addHandler(self.handler)

    def warning(self, msg):
        '''
        Log msg with severity WARNING.
        '''
        self.log.warning('[{date}]: [{clazz}]: [{message}]'.format(date=datetime.now(), clazz=self.__str__(), message=msg))
    
    def info(self, msg):
        '''
        Log msg with severity INFO.
        '''
        self.log.info('[{date}]: [{clazz}]: [{message}]'.format(date=datetime.now(), clazz=self.__str__(), message=msg))
    
    def critical(self, msg):
        '''
        Log msg with severity CRITICAL.
        '''
        self.log.critical('[{date}]: [{clazz}]: [{message}]'.format(date=datetime.now(), clazz=self.__str__(), message=msg))
    
    def error(self, msg):
        '''
        Log msg with severity ERROR.
        '''
        self.log.error('[{date}]: [{clazz}]: [{message}]'.format(date=datetime.now(), clazz=self.__str__(), message=msg))
    
    def __str__(self):
        '''
        Overrides the __str__ function in order to return the class instance name.
        '''
        return self.__class__.__name__
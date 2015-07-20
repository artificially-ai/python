'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''
from threading import Thread
import socket

class SocketServerConn(Thread):
    '''
    '''

    def __init__(self):
        '''
        '''
        Thread.__init__(self)
        self.reopen_sock()
    
    def reopen_sock(self):
        self._socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket_conn.bind(('', 50007))
        self._socket_conn.listen(1)
    
    def run(self):
        self._receive_info('', 50007)
        
    def _receive_info(self, addr, port):
        conn = None
        while True:
            conn, addr = self._socket_conn.accept()
            
            while True:
                try:
                    while 1:
                        data = conn.recv(2048)
                        if not data:
                            break
                        if (data[-1:] == 'E'):
                            print ('ERROR_MESSAGE_ARRIVED: {0}'.format(data))
                            raise socket.error
                        
                        print ('MESSAGE_RECEIVED: {0}'.format(data))
                        
                        if 'END' in data:
                            conn.send('EOF_REACHED')
                        else:
                            conn.send('RECEIVED_SUCESSFULLY')
                except socket.error as error:
                    self._socket_conn.close()
                    self.reopen_sock()
                    
                    if conn:
                        conn.send('RETRY')
                    
                    print (error)
                    
                    continue

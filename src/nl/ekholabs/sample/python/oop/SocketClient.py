'''
Created on Sep 8, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''
from threading import Thread
import socket

class SocketClient(Thread):
    '''
    '''

    def __init__(self):
        '''
        '''
        Thread.__init__(self)
        self._message = ['Hello Socket!', 'Now lets try to break it E', 'And now make it work again']
        
        self.open_sock()
    
    def open_sock(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(('localhost', 50007))
    
    def run(self):
        self._send_info('', 50007)
        
    def _send_info(self, addr, port):
        i = 0
        while True:
            try:
                if i <= 2:
                    self._client.send(self._message[i])
                    i = i + 1
                    
                    data = self._client.recv(2048)
                    print (repr(data))
                else:
                    i = 0
                    self._client.send('EOF')
                    
                    data = self._client.recv(2048)
                    print (repr(data))
            except socket.error as error:
                self._client.close()
                
                self.open_sock()
                print (error)
                
                continue

import sys, random
from PyQt4 import QtGui, QtCore
from GameClient import *

class LoopThread(QtCore.QThread,GameClient):

    update_label_signal = QtCore.pyqtSignal(str)       # create signal
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        GameClient.__init__(self)
        
        
    def connect(self,ip):
        try: 
            self.connect_to_server(ip) #takes what the user entered to the server
        except: return 'no'
                
    def move(self,sms):
        
        self.send_message(sms)
        
    def run(self):          # run executed when start() method called
        
        try:
            while True:
                msg = self.receive_message()
                if len(msg): 
                    self.update_label_signal.emit(str(msg))         #''' emit signal / send message to the main gui '''                    
                else: break
        except Exception as e:
                self.update_label_signal.emit(str(e))    
                 
                print('ERROR:' + str(e) + '\n')
                self.log('ERROR:' + str(e) + '\n')        
        self.update_label_signal.emit(str(msg))    

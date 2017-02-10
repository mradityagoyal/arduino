'''
Created on Feb 10, 2017

@author: agoyal
'''

import time
from PyMata import pymata as pm

class MagicflyBoard:
    BOARD_LED = 13
    
    MAGICFLY_TX_CODE = 0x42         # sysex command code to send code to magicfly
    MAGICFLY_SET_PULSE_WIDTH = 0x43 # sets the pulse width. TODO:
    
    
    def __init__(self, port):
        print("MagicflyBoard init, port: {}".format(port))
        pass
#         self.board = pm.PyMata(port, verbose=True)
    
    def sendCode(self, code):
        """
        Sends the code to magicfly receivers. 
        @param code: the binary code to send.  
        """
        # Set the output to 1 = High
        self.board.digital_write(self.BOARD_LED, 1)
        self.board._command_handler.send_sysex(self.MAGICFLY_TX_CODE, code.encode('utf8'))
        # Wait a half second between toggles.
        time.sleep(.5)
        # Set the output to 0 = Low
        self.board.digital_write(self.BOARD_LED, 0)
        time.sleep(.5)
        
    def set_pulse_width(self, pulseWidth):
        """
        Sends the pulsewidth to use in rcswitch to the arduino. 
        """
        self.board._command_handler.send_sysex(self.MAGICFLY_SET_PULSE_WIDTH, pulseWidth)
    
    def echo_ping(self, msg):
        '''
        prints a string and echoes it back. 
        '''
#         print("echoing: {}".format(msg))
        return msg

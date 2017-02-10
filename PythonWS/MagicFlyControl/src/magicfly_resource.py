'''
Created on Feb 10, 2017

@author: agoyal
'''
import json
import magicfly_board

class MagicflyResource:
    '''
    provides the rest api end points to control the magicfly receivers. 
    Resource acts as web rest api. 
    creates control and sends codes and receives codes. 
    '''
    def __init__(self, port):
        port = "COM3"
        self.magicfly_board = magicfly_board.MagicflyBoard(port)
        


    def on_get(self, req, resp, code):
        '''
        Handles GET Requests
        '''
        #TODO: call the board's sendCode. 
#         self.magicfly_board.sendCode(code)
        ping = self.magicfly_board.echo_ping(code)

        resp.body = json.dumps(ping)
 
    def on_post(self, req, resp):
        '''
        Handles PUT Requests. 
        '''
        pass
 

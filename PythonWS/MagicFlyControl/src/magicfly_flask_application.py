'''
Created on Feb 10, 2017

@author: agoyal
'''
# from flask import Flask
# app = Flask(__name__)
# 
# @app.route("/")
# def hello():
#     return "Hello World!"
# 
# # if __name__ == "__main__":
# #     app.run()



from flask import Flask
import magicfly_board
app = Flask(__name__)
#TODO: find a better way to maintain state. 
data = {}
BASE_URL = '/magicfly/api/v0.1'

@app.route("/")
def hello():
    return "Hello World!"

@app.route((BASE_URL + "/init/<port>"))
def init(port):
    """
    Initializes the magicfly controller on serial port port. 
    @param port: the serial port to use.  
    """
    print(port)
    data["board"]= magicfly_board.MagicflyBoard(port)
    return "Magicfly Board initialized. "

@app.route(BASE_URL + "/echo/<message>")
def test_echoMessage(message):
    """
    Echoes a message all way through to the magicfly_board. 
    """
    board =  data["board"]
    #Find a way to cast as type. 
    return board.echo_ping(message)

@app.route(BASE_URL + "/transmit/<code>")
def transmitCode(code):
    """
    Transmits the binary code using the magicfly board object. 
    @param code: the binary code to send.  
    """
    board =  data["board"]
    board.sendCode(code)
    return "code sent: {}".format(code)

@app.route(BASE_URL + "/pulse/set/<value>")
def set_pulse_width(value):
    """
    Sets the pulse width on the board
    @param value: the pulsewidth to use in the board.  
    """
    board =  data["board"]
    board.set_pulse_width(value)
    return "pulse_width set to: {}".format(value)
    

if __name__ == "__main__":
    app.run()

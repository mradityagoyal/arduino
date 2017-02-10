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
data = {}
BASE_URL = '/magicfly/api/v0.1'

@app.route("/")
def hello():
    return "Hello World!"

@app.route((BASE_URL + "/init/<port>"))
def init(port):
    print(port)
    data["board"]= magicfly_board.MagicflyBoard(port)
    return "Magicfly Board initialized. "

@app.route(BASE_URL + "/echo/<message>")
def getBoard(message):
    board =  data["board"]
    return board.echo_ping(message)

@app.route(BASE_URL + "/transmit/<code>")
def transmitCode(code):
    board =  data["board"]
    board.sendCode(code)
    return "code sent: {}".format(code)

if __name__ == "__main__":
    app.run()

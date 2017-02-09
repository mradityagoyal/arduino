'''
This code contains starting python code example for arduino pymata testing.
'''

import time
import sys
import signal

from PyMata.pymata import PyMata


# create a PyMata instance
board = PyMata("COM", verbose=True)

# you may need to press ctrl c twice
def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
        board.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Configure the trigger and echo pins

time.sleep(1)

# Create a forever loop that will print out the sonar data for the PING device

while 1:
    data = board.digital_write(13, 1)
    print(str(data[2]) + ' centimeters')
    time.sleep(.2)

# TODO: add pin for transmission.

def magicfly_control(self, data):
    """
    Transmits the given code over 433 mhz radio frequency. The bitlength and pulseLenght are used in RC-Switch library.
    :param self: self obj
    :param data: data to send
    :return:
    """


def transmit_magicfly():
    """
    Initially.. let's just try to send a predefined stuff.
    // stepper motor configuration message definition for 2 conductor motor
  0  START_SYSEX                     (0xF0)
  1  MAGICFLY_CONTROL                    (0x42)
  2  TRANSMIT               (0x00)
  3  PULSE_LENGTH            length of pulse
  3  BIT_LENGTH              length of bit
  4  DATA (BIT LENGTH number of bytes)
  7  END_SYSEX (0xF7)
    :return:
    """

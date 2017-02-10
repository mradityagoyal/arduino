'''
This code contains starting python code example for arduino pymata testing.
'''

import time
import sys
import signal

from PyMata.pymata import PyMata
from binascii import unhexlify


# Digital pin 13 is connected to an LED. If you are running this script with
# an Arduino UNO no LED is needed (Pin 13 is connected to an internal LED).
BOARD_LED = 13
MAGICFLY_CONTROL = 0x42

# Create a PyMata instance
board = PyMata("/COM3", verbose=True)

def toFirmataFormat(str):
    data = bytearray()
    for b in str.encode('utf8'):
        data.append(b & 0x7F)
        data.append((b >> 7) & 0x7F)
    return data

def long_to_bytes (val):
    return [val & 0x7f, (val & 0x7F00)>>7, (val & 0x7f0000) >> 16, (val & 0x7f0000)>>24]

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Set digital pin 13 to be an output port
board.set_pin_mode(BOARD_LED, board.OUTPUT, board.DIGITAL)

time.sleep(2)
print("Blinking LED on pin 13 for 10 times ...")

# Blink for 10 times
for x in range(2):
    print(x + 1)
    # Set the output to 1 = High
    board.digital_write(BOARD_LED, 1)
    code = "101101111101010000000100".encode('utf8')
    board._command_handler.send_sysex(MAGICFLY_CONTROL, code)
    # Wait a half second between toggles.
    time.sleep(.5)
    # Set the output to 0 = Low
    board.digital_write(BOARD_LED, 0)
    time.sleep(.5)

# Close PyMata when we are done
board.close()

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

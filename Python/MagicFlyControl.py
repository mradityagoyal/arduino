'''
This code contains starting python code example for arduino pymata testing.
'''


def transmitCode(self, code, bitLength, pulseLength):
    """
    Transmits the given code over 433 mhz radio frequency. The bitlength and pulseLenght are used in RC-Switch library.
    :param self: self obj
    :param code: The binary code to transmit
    :param bitLength: the bitlength of the message
    :param pulseLength: pulseLength to use in rc-switch
    :return:
    """


def sniffCode(self, data, timeout = 20):
    """
    This mthod sniffs the code from the 433 mhz receiver using rc-switch
    :param self:
    :param data:
    :param timeout: the max timeout to allow arduino to respond
    :return:
    """

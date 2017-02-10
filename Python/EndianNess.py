from binascii import unhexlify

def long_to_bytes (val):
    return [val & 0x7f, (val & 0x7F00)>>7, (val & 0x7f0000) >> 15, (val & 0x7f000000)>>23]

def bytes_to_long(argv):
    return argv[3]<<23|argv[2]<<15|argv[1]<<7|argv[0];

val = 12047363

bytes = long_to_bytes(val)

ret_val = bytes_to_long(bytes)

v1 = oct(val & 0x7f)
v2 = oct((val & 0xFF00))
v3 = oct((val & 0x7f0000) >> 15)
v4 = oct((val & 0x7f000000)>>23)

# print("V1 {}".format(v1))
# print("V2 {}".format(v2))
# print("V3 {}".format(v3))
# print("V4 {}".format(v4))
#
#
# print(oct(val))
# print(long_to_bytes(val))
#
# print(ret_val)
# print(long_to_bytes(7251971))


def toFirmataFormat(str):
    data = bytearray()
    for b in str.encode('utf8'):
        data.append(b & 0x7F)
        data.append((b >> 7) & 0x7F)
    return data

# data = toFirmataFormat("101101111101010000000100")
# for b in data:
#     print(b)

str = "aditya".encode('utf8')

for a in str:
    print(type(a))
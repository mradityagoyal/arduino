def toFirmataFormat(str):
    data = bytearray()
    for b in str.encode('utf8'):
        data.append(b & 0x7F)
        data.append((b >> 7) & 0x7F)
    return data

def long_to_bytes (val):
    return [val & 0x7f, (val & 0x7F00)>>7, (val & 0x7f0000) >> 16, (val & 0x7f0000)>>24]


print('haha '+'nono')
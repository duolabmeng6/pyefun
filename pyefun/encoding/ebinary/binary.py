import binascii

def binary编码(data):
    if (type(data) == str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data
    return binascii.b2a_hex(data_bytes)


def binary解码(data):
    return binascii.a2b_hex(data)

import zlib
import binascii


def zlib压缩(data):
    return zlib.compress(data)

def zlib解压(data):
    return zlib.decompress(data)

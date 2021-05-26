import unittest

from .ezlib import *


class Testezlib(unittest.TestCase):

    def test_1(self):
        data = zlib压缩(b"1234567890")

        self.assertEqual(binascii.hexlify(data), b"789c33343236313533b7b03400000b2c020e")

        ddata = zlib解压(data)

        self.assertEqual(ddata, b"1234567890")

        # print('压缩的数据:长度 : {},内容 : {}'.format(len(data), ddata))

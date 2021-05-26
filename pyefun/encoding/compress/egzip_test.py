import unittest

from .egzip import *
import binascii


class Testegzip(unittest.TestCase):

    def test_1(self):
        data = gzip压缩(b"1234567890")
        print("压缩后大小 %s" % len(data)  )

        ddata = gzip解压(data)

        self.assertEqual(ddata, b"1234567890")

        # print('压缩的数据:长度 : {},内容 : {}'.format(len(data), ddata))

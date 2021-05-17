import unittest

from .systemProcessingBase import *


class TestSystemProcessingBase(unittest.TestCase):

    def test_1(self):
        pass
        data = 运行("ipconfig")
        print(data)

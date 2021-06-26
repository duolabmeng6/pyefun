import unittest

from .arithmeticOperationBase import *
from .typeConv import *

class TestDirk(unittest.TestCase):

    def test_1(self):
        pass
        self.assertEqual(四舍五入(123.144, 2), 123.14)
        self.assertEqual(四舍五入(123.146, 2), 123.15)
        self.assertEqual(取绝对值(-1), 1)

        self.assertEqual(取绝对值(-100), 100)
        self.assertEqual(取绝对值(-0.1), 0.1)
        self.assertEqual(取绝对值(0.1), 0.1)

        self.assertEqual(取整(100.111), 100)
        self.assertEqual(到整数('8852791.5'), 8852791)
        self.assertEqual(到整数('-8852791.5'), -8852791)
        self.assertEqual(到整数('8852791.5123456789'), 8852791)
        self.assertEqual(到整数('-8852791.5123456789'), -8852791)

        self.assertEqual(求次方(2, 2), 4)
        self.assertEqual(求次方(4, 2), 16)
        self.assertEqual(求余弦(30), 0.15425144988758405)
        self.assertEqual(求反正切(30), 1.5374753309166493)
        self.assertEqual(求平方根(2), 1.4142135623730951)
        self.assertEqual(求正切(30), -6.405331196646276)
        self.assertEqual(求正弦(30), -0.9880316240928618)
        self.assertEqual(取随机数(1, 1), 1)
        self.assertEqual(取整数('8852791.5'), 8852791)
        self.assertEqual(取整数('+8852791.5'), 8852791)
        self.assertEqual(取整数('-8852791.5'), -8852791)
        self.assertEqual(取整数(8852791.5), 8852791)


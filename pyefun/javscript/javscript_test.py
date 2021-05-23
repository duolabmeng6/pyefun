import unittest

from .javscript import *


class TestJs(unittest.TestCase):

    def test_1(self):
        pass
        js = javscript("JScript")
        data = js.运行("1 + 2")
        self.assertEqual(data, 3)

        js = javscript("Node")
        data = js.运行("1 + 2")
        self.assertEqual(data, 3)

        js = javscript("Node")
        js.加载代码(""" 
        function add(x, y) { 
          return x + y; 
        } 
        """)
        data = js.执行("add", 1, 2)
        self.assertEqual(data, 3)
        data = js.运行("add(1,2)")
        self.assertEqual(data, 3)

        data = 运行js(""" 
        function add(x, y) { 
          return x + y; 
        } 
        """, "add(1,2)")
        self.assertEqual(data, 3)

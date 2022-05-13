# 教程
# https://pandas.pydata.org/pandas-docs/stable/index.html

import pandas
from pyefun import *


class 数据分析():
    def __init__(self, 文件名):
        扩展名 = 文件_取扩展名(文件名)
        if 扩展名 == "xlsx":
            self.pd = pandas.read_excel(文件名)
        elif 扩展名 == "csv":
            self.pd = pandas.read_csv(文件名)

    def __str__(self, instance, value):
        return self.pd


def 测试函数():
    data = 数据分析("../excel/test.xlsx")
    print(data)


测试函数()

import os
import sys
import zipfile

#
# def rename(pwd: str, filename=''):
#     """压缩包内部文件有中文名, 解压后出现乱码，进行恢复"""
#
#     path = f'{pwd}/{filename}'
#     if os.path.isdir(path):
#         for i in os.scandir(path):
#             rename(path, i.name)
#     newname = filename.encode('cp437').decode('gbk')
#     os.rename(path, f'{pwd}/{newname}')


"""
zip文件解压缩

https://docs.python.org/zh-cn/3.9/library/zipfile.html?highlight=zipfile#


"""

import zipfile
from pyefun import *
import pyefun.commonlyUtil as commonlyUtil

@异常处理返回类型逻辑型
def zip解压(压缩包的路径: str, 解压路径: str):
    file = zipfile.ZipFile(压缩包的路径)
    if 文件是否存在(解压路径) == False:
        commonlyUtil.目录_创建(解压路径)
    file.extractall(解压路径)
    file.close()


@异常处理返回类型逻辑型
def zip压缩(保存压缩包的路径: str, 欲压缩文件或者文件夹: str,mode="w"):
    pass
    保存压缩包的路径 = 路径_优化路径(保存压缩包的路径)
    欲压缩文件或者文件夹 = 路径_优化路径(欲压缩文件或者文件夹)
    路径字符长度 = 取文本长度(欲压缩文件或者文件夹)
    if 文件_是否为文件(欲压缩文件或者文件夹):
        with zipfile.ZipFile(保存压缩包的路径, mode=mode) as target:
            target.write(欲压缩文件或者文件夹, 文件_取文件名(欲压缩文件或者文件夹))
        return True
    if 文件_是否为目录(欲压缩文件或者文件夹):
        with zipfile.ZipFile(保存压缩包的路径, mode=mode) as target:
            压缩文件列表 = []
            for 路径信息 in os.walk(欲压缩文件或者文件夹):
                for 文件名 in 路径信息[2]:
                    目录 = 路径信息[0]
                    文件路径 = 路径_合并(目录, 文件名)
                    相对路径 = 取文本右边(文件路径, 取文本长度(文件路径) - 路径字符长度)
                    if(文件路径 == 保存压缩包的路径):
                        continue
                        # 防止死循环一直压缩
                    压缩文件列表.append([文件路径,相对路径])

            # 开始压缩
            for item in 压缩文件列表:
                文件路径 = item[0]
                相对路径 = item[1]
                target.write(文件路径, 相对路径)
        return True

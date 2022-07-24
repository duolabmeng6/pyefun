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


@异常处理返回类型逻辑型
def zip解压(压缩包的路径: str, 解压路径: str):
    file = zipfile.ZipFile(压缩包的路径)
    if not 文件是否存在(解压路径):
        创建目录(解压路径)
    file.extractall(解压路径)
    file.close()


@异常处理返回类型逻辑型
def zip压缩(保存压缩包的路径: str, 欲压缩文件或者文件夹: str, mode="w"):
    pass
    保存压缩包的路径 = 路径优化(保存压缩包的路径)
    欲压缩文件或者文件夹 = 路径优化(欲压缩文件或者文件夹)
    路径字符长度 = 取文本长度(欲压缩文件或者文件夹)
    if 文件_是否为文件(欲压缩文件或者文件夹):
        with zipfile.ZipFile(保存压缩包的路径, mode=mode) as target:
            target.write(欲压缩文件或者文件夹, 文件_取文件名(欲压缩文件或者文件夹), zipfile.ZIP_DEFLATED)
        return True
    if 文件_是否为目录(欲压缩文件或者文件夹):
        # 检查后缀是否有 "/"
        if 欲压缩文件或者文件夹[-1] == "/":
            欲压缩文件或者文件夹.lstrip("/")

        父目录 = 文件_取父目录(欲压缩文件或者文件夹)
        路径字符长度 = 取文本长度(父目录) + 1

        with zipfile.ZipFile(保存压缩包的路径, mode=mode) as target:
            压缩文件列表 = []
            for 路径信息 in os.walk(欲压缩文件或者文件夹):
                for 文件名 in 路径信息[2]:
                    目录 = 路径信息[0]
                    文件路径 = 路径_合并(目录, 文件名)
                    相对路径 = 取文本右边(文件路径, 取文本长度(文件路径) - 路径字符长度)
                    if 文件路径 == 保存压缩包的路径:
                        continue
                        # 防止死循环一直压缩
                    压缩文件列表.append([文件路径, 相对路径])

            # 开始压缩
            for item in 压缩文件列表:
                文件路径 = item[0]
                相对路径 = item[1]
                if os.path.islink(文件路径):
                    # http://www.mail-archive.com/python-list@python.org/msg34223.html
                    压缩包信息 = zipfile.ZipInfo(相对路径)
                    压缩包信息.create_system = 3
                    # long type of hex val of '0xA1ED0000L',
                    # 建立软连接
                    压缩包信息.external_attr = 2716663808
                    target.writestr(压缩包信息, os.readlink(文件路径))
                else:
                    target.write(文件路径, 相对路径, zipfile.ZIP_DEFLATED)
        return True


@异常处理返回类型逻辑型
def zip压缩2(压缩包的路径, 待压缩的文件或目录):
    # 使用递归实现的压缩
    with zipfile.ZipFile(压缩包的路径, 'w', compression=zipfile.ZIP_DEFLATED) as 压缩包文件:
        父目录文本长度 = len(os.path.dirname(待压缩的文件或目录))

        def 递归压缩(父目录):
            文件路径列表 = os.listdir(父目录)
            if not 文件路径列表:
                # http://www.velocityreviews.com/forums/t318840-add-empty-directory-using-zipfile.html
                根目录 = 父目录[父目录文本长度:].replace('\\', '/').lstrip('/')
                压缩包信息 = zipfile.ZipInfo(根目录 + '/')
                压缩包文件.writestr(压缩包信息, '')
            for 路径 in 文件路径列表:
                文件绝对路径 = os.path.join(父目录, 路径)
                if os.path.isdir(文件绝对路径) and not os.path.islink(文件绝对路径):
                    递归压缩(文件绝对路径)
                else:
                    根目录 = 文件绝对路径[父目录文本长度:].replace('\\', '/').lstrip('/')
                    if os.path.islink(文件绝对路径):
                        # http://www.mail-archive.com/python-list@python.org/msg34223.html
                        压缩包信息 = zipfile.ZipInfo(根目录)
                        压缩包信息.create_system = 3
                        # long type of hex val of '0xA1ED0000L',
                        # 建立软连接
                        压缩包信息.external_attr = 2716663808
                        压缩包文件.writestr(压缩包信息, os.readlink(文件绝对路径))
                    else:
                        压缩包文件.write(文件绝对路径, 根目录, zipfile.ZIP_DEFLATED)

        递归压缩(待压缩的文件或目录)
    return True


@异常处理返回类型逻辑型
def zip解压2(压缩包的路径, 解压目录, 允许解压路径前缀=[]):
    # 保持权限和软连接解压
    # 允许解压路径前缀 例如 ["my_app.app/Contents/"] 不填则全部解压

    file = zipfile.ZipFile(压缩包的路径)
    for info in file.infolist():
        # 检查 目标文件路径 是否在 允许解压路径前缀 中
        if len(允许解压路径前缀) > 0:
            允许解压 = False
            for 路径 in 允许解压路径前缀:
                if info.filename.startswith(路径):
                    允许解压 = True
            if not 允许解压:
                # print("不允许解压", info.filename)
                continue

        文件名 = info.filename
        try:
            info.filename = 文件名.encode('cp437').decode('utf-8')
        except:
            pass
        目标文件路径 = os.path.join(解压目录, info.filename)
        # 解压
        权限 = info.external_attr >> 16
        if stat.S_ISLNK(权限):  # 权限 == 'lrwxr-xr-x' 权限 = stat.filemode(hi)
            软连接位置 = file.open(info).read()  # 读入软连接的位置
            # 检查 目标文件路径 是否存在，如果存在就删除 防止创建失败
            if os.path.exists(目标文件路径):
                os.remove(目标文件路径)
            # ic(目标文件路径, 软连接位置)
            os.symlink(软连接位置, 目标文件路径)
        else:
            # 删除文件 重新解压
            # print("解压", 文件名)
            if os.path.exists(目标文件路径):
                # 检查是否为文件
                if os.path.isfile(目标文件路径):
                    os.remove(目标文件路径)
            file.extract(info, path=解压目录)
            os.chmod(目标文件路径, 权限)
    return True


def zip解压系统命令(压缩包的路径, 解压目录):
    # 仅适用于linux macos
    运行命令 = "unzip -o " + 压缩包的路径 + " -d " + 解压目录
    os.system(运行命令)

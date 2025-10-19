"""

.. Hint::
    图像处理

    pip install pillow

.. literalinclude:: ../../../pyefun/imageUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:


"""
import os

from PIL import Image, ImageGrab
import io


def image到字节集(image对象):
    字节流 = io.BytesIO()
    image对象.save(字节流, format='PNG')
    图片字节集 = 字节流.getvalue()
    字节流.close()
    return 图片字节集


def image从字节集加载(图片字节集) -> Image:
    return Image.open(io.BytesIO(图片字节集))


def 图片_修改尺寸(图片路径, 保存地址, 横=100, 竖=100):
    im = Image.open(图片路径)
    dImg = im.resize((横, 竖), Image.ANTIALIAS)  # 横竖长度
    dImg.save(保存地址)


def 图片_压缩(infile, outfile='', mb=150, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = os.path.getsize(infile) / 1024
    if o_size <= mb:
        return infile

    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = os.path.getsize(outfile) / 1024
    return outfile, os.path.getsize(outfile) / 1024


def 截图_取当前屏幕(图片路径="picture.jpg"):
    """
    保存在当前目录下picture.jpg文件
    """
    pic = ImageGrab.grab()
    pic.save(图片路径)

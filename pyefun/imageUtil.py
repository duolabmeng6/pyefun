"""

.. Hint::
    图像处理

    pip install pillow

.. literalinclude:: ../../../pyefun/imageUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:


"""
from PIL import Image,ImageGrab
import io


def image到字节集(image对象):
    字节流 = io.BytesIO()
    image对象.save(字节流, format='PNG')
    图片字节集 = 字节流.getvalue()
    字节流.close()
    return 图片字节集


def image从字节集加载(图片字节集) -> Image:
    return Image.open(io.BytesIO(图片字节集))


def image取图片宽度高度(image对象: Image.Image):
    width, height = image对象.size
    return width, height

def image显示图片(image对象):
    image对象.show()

def 图片_修改_尺寸(path,保存地址,横=100,竖=100):
    im=Image.open(path)
    w,h=im.size
    print(w,h)
    dImg = im.resize((横, 竖), Image.ANTIALIAS)#横竖长度
    dImg.save(保存地址)
    print("修改完成",保存地址)
def 图片_压缩_大小(infile, outfile='', mb=150, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = os.path.getsize(infile)/ 1024
    if o_size <= mb:
        return infile

    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = os.path.getsize(outfile)/ 1024
    return outfile, os.path.getsize(outfile)/ 1024
def 截图_截取当前屏幕():
    """
    保存在当前目录下picture.jpg文件
    """
    pic = ImageGrab.grab()
    pic.save("picture.jpg")
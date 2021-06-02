"""

.. Hint::
    图像处理

    pip install pillow

.. literalinclude:: ../../../pyefun/imageUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:


"""
from PIL import Image
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
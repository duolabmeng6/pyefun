"""

.. Hint::
    二维码编码解码操作

    https://github.com/lincolnloop/python-qrcode

    需要安装

    pip install qrcode

    pip install pyzbar

.. literalinclude:: ../../../pyefun/qrcode/eqrcode_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
import qrcode
from PIL import Image
import pyzbar.pyzbar as pyzbar
from io import BytesIO


def 二维码识别(图像字节集):
    pass
    try:
        return str(pyzbar.decode(Image.open(BytesIO(图像字节集)), symbols=[pyzbar.ZBarSymbol.QRCODE])[0][0],
                   encoding="utf-8")
    except:
        return ""


def 二维码生成(编码数据, 优化级别=20, 纠错级别=qrcode.constants.ERROR_CORRECT_M, 格子像素数=10, 边框留白=4):
    """
    error_correction:控制二维码纠错级别。
    ERROR_CORRECT_L:大约7%或者更少的错误会被更正。
    ERROR_CORRECT_M:默认值，大约15%或者更少的错误会被更正。
    ERROR_CORRECT_Q:大约25%或者更少的错误会被更正。
    ERROR_CORRECT_H:大约30%或者更少的错误会被更正。
    box_size:控制二维码中每个格子的像素数，默认为10。
    border:控制二维码四周留白包含的格子数，默认为4。
    image_factory:选择生成图片的形式，默认为PIL图像。
    mask_pattern:选择生成图片的的掩模。

 """
    qr = qrcode.QRCode(
        version=1,
        error_correction=纠错级别,
        box_size=格子像素数,
        border=边框留白)
    qr.add_data(编码数据, optimize=优化级别)
    qr.make()

    im = qr.make_image().get_image()

    img_byte = BytesIO()
    im.save(img_byte, format='png')
    binary_content = img_byte.getvalue()
    img_byte.close()

    return binary_content

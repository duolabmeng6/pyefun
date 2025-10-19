import base64
from io import BytesIO

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter


class 图像操作PIL类(object):
    """
    图像操作类PIL
    本类用于对图像进行操作 使用PIL库
    """

    def __init__(self, obj=None):
        # print(type(obj))
        """
        __init__ 的功能说明（请补充）。

        Args:
            obj (可选): 参数说明。默认值为 None。

        """
        if type(obj) == str:
            self.img = Image.open(obj)
        else:
            self.img = obj

    def 加载图片(self, image_path):
        """
        加载图片 的功能说明（请补充）。

        Args:
            image_path: 参数说明。

        """
        self.img = Image.open(image_path)

    def 加载图片从base64(self, base64_str):
        """
        加载图片从base64 的功能说明（请补充）。

        Args:
            base64_str: 参数说明。

        """
        img_io = BytesIO(base64.b64decode(base64_str))
        self.img = Image.open(img_io)
        return self

    def 创建空白图片(self, w, h, color=(255, 255, 255)):
        """
        创建空白图片 的功能说明（请补充）。

        Args:
            w: 参数说明。
            h: 参数说明。
            color (可选): 参数说明。默认值为 (255, 255, 255)。

        """
        self.img = Image.new('RGB', (w, h), color)
        return self

    def 绘制图片(self, img, x1=0, y1=0, w=100, h=100):
        """
        绘制图片 的功能说明（请补充）。

        Args:
            img: 参数说明。
            x1 (可选): 参数说明。默认值为 0。
            y1 (可选): 参数说明。默认值为 0。
            w (可选): 参数说明。默认值为 100。
            h (可选): 参数说明。默认值为 100。

        """
        self.img.paste(img, (x1, y1, w, h))

    def 到数据(self):
        """
        到数据 的功能说明（请补充）。

        """
        return np.array(self.img)

    def 显示图片(self):
        """
        显示图片 的功能说明（请补充）。

        """
        data = np.array(self.img)[..., ::-1]
        cv2.imshow("show", data)
        cv2.waitKey(0)
        return self

    # 显示图片 系统打开图片的方式
    def 显示图片2(self):
        """
        显示图片2 的功能说明（请补充）。

        """
        self.img.show()

    # 剪裁图片
    def 剪裁(self, x1, y1, w, h):
        """
        剪裁 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。
            w: 参数说明。
            h: 参数说明。

        """
        self.img = self.img.crop((x1, y1, w, h))
        return self

    # 保存为文件
    def 保存为文件(self, path):
        """
        保存为文件 的功能说明（请补充）。

        Args:
            path: 参数说明。

        """
        self.img.save(path)
        return self

    # 二值化
    def 二值化(self, threshold=127):
        """
        二值化 的功能说明（请补充）。

        Args:
            threshold (可选): 参数说明。默认值为 127。

        """
        self.img = self.img.convert('L')
        self.img = self.img.point(lambda x: 0 if x < threshold else 255, '1')
        return self

    # 绘制矩形
    def 绘制矩形(self, x1, y1, w, h, color=(255, 0, 0), width=1):
        """
        绘制矩形 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。
            w: 参数说明。
            h: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。
            width (可选): 参数说明。默认值为 1。

        """
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((x1, y1, w, h), outline=color, width=width)
        return self

    # 绘制文本汉字
    def 绘制文本(self, text, x1, y1, color=(255, 0, 0), font_size=20):
        """
        绘制文本 的功能说明（请补充）。

        Args:
            text: 参数说明。
            x1: 参数说明。
            y1: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。
            font_size (可选): 参数说明。默认值为 20。

        """
        draw = ImageDraw.Draw(self.img)
        font = ImageFont.truetype("msyh.ttc", font_size, encoding="utf-8")
        draw.text((x1, y1), text, color, font)
        return self

    # 绘制填充矩形
    def 绘制填充矩形(self, x1, y1, x2, y2, color=(255, 0, 0), 透明度=0.5):
        """
        绘制填充矩形 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。
            x2: 参数说明。
            y2: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。
            透明度 (可选): 参数说明。默认值为 0.5。

        """
        h, w = self.img.height, self.img.width
        img_left = self.img.copy()
        draw_left = ImageDraw.Draw(img_left)
        draw_left.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], outline=color, fill=color)
        img_left = Image.blend(self.img, img_left, 透明度)
        img_show = Image.new('RGB', (w, h), (255, 255, 255))
        img_show.paste(img_left, (0, 0, w, h))
        self.img = np.array(img_show)
        return self

    # 绘制多边形
    def 绘制多边形(self, points, color=(255, 0, 0)):
        """
        绘制多边形 的功能说明（请补充）。

        Args:
            points: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。

        """
        draw_left = ImageDraw.Draw(self.img)
        draw_left.polygon(np.array(points, dtype=np.float32), outline=color)
        return self

    # 绘制填充多边形
    def 绘制填充多边形(self, points, color=(255, 0, 0), 透明度=0.5):
        """
        绘制填充多边形 的功能说明（请补充）。

        Args:
            points: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。
            透明度 (可选): 参数说明。默认值为 0.5。

        """
        h, w = self.img.height, self.img.width
        img_left = self.img.copy()
        draw_left = ImageDraw.Draw(img_left)
        draw_left.polygon(np.array(points, dtype=np.float32), outline=color, fill=color)
        img_left = Image.blend(self.img, img_left, 透明度)
        img_show = Image.new('RGB', (w, h), (255, 255, 255))
        img_show.paste(img_left, (0, 0, w, h))
        self.img = np.array(img_show)
        return self

    # 到base64
    def 到base64(self):
        """
        到base64 的功能说明（请补充）。

        """
        img_io = BytesIO()
        self.img.save(img_io, 'JPEG')
        img_io.seek(0)
        return base64.b64encode(img_io.getvalue()).decode()

    # 黑白颜色反转
    def 颜色翻转(self):
        """
        颜色翻转 的功能说明（请补充）。

        """
        self.img = self.img.convert('L')
        return self

    def 图像翻转左右(self):
        """
        图像翻转左右 的功能说明（请补充）。

        """
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        return self

    def 图像翻转上下(self):
        """
        图像翻转上下 的功能说明（请补充）。

        """
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        return self

    def 图像翻转180(self):
        """
        图像翻转180 的功能说明（请补充）。

        """
        self.img = self.img.transpose(Image.ROTATE_180)
        return self

    def 图像翻转90(self):
        """
        图像翻转90 的功能说明（请补充）。

        """
        self.img = self.img.transpose(Image.ROTATE_90)
        return self

    def 图像翻转270(self):
        """
        图像翻转270 的功能说明（请补充）。

        """
        self.img = self.img.transpose(Image.ROTATE_270)
        return self

    @property
    def 宽度(self):
        """
        宽度 的功能说明（请补充）。

        """
        return self.img.width

    @property
    def 高度(self):
        """
        高度 的功能说明（请补充）。

        """
        return self.img.height

    def 取所有颜色(self):
        """
        取所有颜色 的功能说明（请补充）。

        """
        return self.img.getcolors()

    def 绘制点(self, x1, y1, color=(255, 0, 0)):
        """
        绘制点 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。

        """
        draw = ImageDraw.Draw(self.img)
        draw.point((x1, y1), color)
        return self

    def 取颜色(self, x1, y1):
        """
        取颜色 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。

        """
        return self.img.getpixel((x1, y1))

    # 绘制圆形
    def 绘制圆形(self, x1, y1, r, color=(255, 0, 0), width=1):
        """
        绘制圆形 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。
            r: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。
            width (可选): 参数说明。默认值为 1。

        """
        draw = ImageDraw.Draw(self.img)
        draw.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), outline=color, width=width)
        return self

    # 绘制填充圆形
    def 绘制填充圆形(self, x1, y1, r, color=(255, 0, 0), 透明度=0.5):
        """
        绘制填充圆形 的功能说明（请补充）。

        Args:
            x1: 参数说明。
            y1: 参数说明。
            r: 参数说明。
            color (可选): 参数说明。默认值为 (255, 0, 0)。
            透明度 (可选): 参数说明。默认值为 0.5。

        """
        h, w = self.img.height, self.img.width
        img_left = self.img.copy()
        draw_left = ImageDraw.Draw(img_left)
        draw_left.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), outline=color, fill=color)
        img_left = Image.blend(self.img, img_left, 透明度)
        img_show = Image.new('RGB', (w, h), (255, 255, 255))
        img_show.paste(img_left, (0, 0, w, h))
        self.img = np.array(img_show)
        return self

    # 增强对比度
    def 增强对比度(self, 增强倍数=1.5):
        """
        增强对比度 的功能说明（请补充）。

        Args:
            增强倍数 (可选): 参数说明。默认值为 1.5。

        """
        self.img = ImageEnhance.Contrast(self.img).enhance(增强倍数)
        return self

    # 增强亮度
    def 增强亮度(self, 增强倍数=1.5):
        """
        增强亮度 的功能说明（请补充）。

        Args:
            增强倍数 (可选): 参数说明。默认值为 1.5。

        """
        self.img = ImageEnhance.Brightness(self.img).enhance(增强倍数)
        return self

    # 重置图片大小
    def 重置图片大小(self, 宽度, 高度):
        """
        重置图片大小 的功能说明（请补充）。

        Args:
            宽度: 参数说明。
            高度: 参数说明。

        """
        self.img = self.img.resize((宽度, 高度))
        return self
    # 缩放
    def 缩放(self, 缩放倍数):
        """
        缩放 的功能说明（请补充）。

        Args:
            缩放倍数: 参数说明。

        """
        self.img = self.img.resize((int(self.img.width * 缩放倍数), int(self.img.height * 缩放倍数)))
        return self

    # 清晰度
    def 清晰度(self, 增减倍数=1.5):
        """
        清晰度 的功能说明（请补充）。

        Args:
            增减倍数 (可选): 参数说明。默认值为 1.5。

        """
        self.img = ImageEnhance.Sharpness(self.img).enhance(增减倍数)
        return self

    # 高斯模糊
    def 高斯模糊(self, 模糊半径=10):
        """
        高斯模糊 的功能说明（请补充）。

        Args:
            模糊半径 (可选): 参数说明。默认值为 10。

        """
        self.img = self.img.filter(ImageFilter.GaussianBlur(模糊半径))
        return self

    # 边缘检测
    def 边缘检测(self):
        """
        边缘检测 的功能说明（请补充）。

        """
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        return self

    # 轮廓
    def 轮廓(self):
        """
        轮廓 的功能说明（请补充）。

        """
        self.img = self.img.filter(ImageFilter.CONTOUR)
        return self


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
        if type(obj) == str:
            self.img = Image.open(obj)
        else:
            self.img = obj

    def 加载图片(self, image_path):
        self.img = Image.open(image_path)

    def 加载图片从base64(self, base64_str):
        img_io = BytesIO(base64.b64decode(base64_str))
        self.img = Image.open(img_io)
        return self

    def 创建空白图片(self, w, h, color=(255, 255, 255)):
        self.img = Image.new('RGB', (w, h), color)
        return self

    def 绘制图片(self, img, x1=0, y1=0, w=100, h=100):
        self.img.paste(img, (x1, y1, w, h))

    def 到数据(self):
        return np.array(self.img)

    def 显示图片(self):
        data = np.array(self.img)[..., ::-1]
        cv2.imshow("show", data)
        cv2.waitKey(0)
        return self

    # 显示图片 系统打开图片的方式
    def 显示图片2(self):
        self.img.show()

    # 剪裁图片
    def 剪裁(self, x1, y1, w, h):
        self.img = self.img.crop((x1, y1, w, h))
        return self

    # 保存为文件
    def 保存为文件(self, path):
        self.img.save(path)
        return self

    # 二值化
    def 二值化(self, threshold=127):
        self.img = self.img.convert('L')
        self.img = self.img.point(lambda x: 0 if x < threshold else 255, '1')
        return self

    # 绘制矩形
    def 绘制矩形(self, x1, y1, w, h, color=(255, 0, 0), width=1):
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((x1, y1, w, h), outline=color, width=width)
        return self

    # 绘制文本汉字
    def 绘制文本(self, text, x1, y1, color=(255, 0, 0), font_size=20):
        draw = ImageDraw.Draw(self.img)
        font = ImageFont.truetype("msyh.ttc", font_size, encoding="utf-8")
        draw.text((x1, y1), text, color, font)
        return self

    # 绘制填充矩形
    def 绘制填充矩形(self, x1, y1, x2, y2, color=(255, 0, 0), 透明度=0.5):
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
        draw_left = ImageDraw.Draw(self.img)
        draw_left.polygon(np.array(points, dtype=np.float32), outline=color)
        return self

    # 绘制填充多边形
    def 绘制填充多边形(self, points, color=(255, 0, 0), 透明度=0.5):
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
        img_io = BytesIO()
        self.img.save(img_io, 'JPEG')
        img_io.seek(0)
        return base64.b64encode(img_io.getvalue()).decode()

    # 黑白颜色反转
    def 颜色翻转(self):
        self.img = self.img.convert('L')
        return self

    def 图像翻转左右(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        return self

    def 图像翻转上下(self):
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        return self

    def 图像翻转180(self):
        self.img = self.img.transpose(Image.ROTATE_180)
        return self

    def 图像翻转90(self):
        self.img = self.img.transpose(Image.ROTATE_90)
        return self

    def 图像翻转270(self):
        self.img = self.img.transpose(Image.ROTATE_270)
        return self

    @property
    def 宽度(self):
        return self.img.width

    @property
    def 高度(self):
        return self.img.height

    def 取所有颜色(self):
        return self.img.getcolors()

    def 绘制点(self, x1, y1, color=(255, 0, 0)):
        draw = ImageDraw.Draw(self.img)
        draw.point((x1, y1), color)
        return self

    def 取颜色(self, x1, y1):
        return self.img.getpixel((x1, y1))

    # 绘制圆形
    def 绘制圆形(self, x1, y1, r, color=(255, 0, 0), width=1):
        draw = ImageDraw.Draw(self.img)
        draw.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), outline=color, width=width)
        return self

    # 绘制填充圆形
    def 绘制填充圆形(self, x1, y1, r, color=(255, 0, 0), 透明度=0.5):
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
        self.img = ImageEnhance.Contrast(self.img).enhance(增强倍数)
        return self

    # 增强亮度
    def 增强亮度(self, 增强倍数=1.5):
        self.img = ImageEnhance.Brightness(self.img).enhance(增强倍数)
        return self

    # 重置图片大小
    def 重置图片大小(self, 宽度, 高度):
        self.img = self.img.resize((宽度, 高度))
        return self
    # 缩放
    def 缩放(self, 缩放倍数):
        self.img = self.img.resize((int(self.img.width * 缩放倍数), int(self.img.height * 缩放倍数)))
        return self

    # 清晰度
    def 清晰度(self, 增减倍数=1.5):
        self.img = ImageEnhance.Sharpness(self.img).enhance(增减倍数)
        return self

    # 高斯模糊
    def 高斯模糊(self, 模糊半径=10):
        self.img = self.img.filter(ImageFilter.GaussianBlur(模糊半径))
        return self

    # 边缘检测
    def 边缘检测(self):
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        return self

    # 轮廓
    def 轮廓(self):
        self.img = self.img.filter(ImageFilter.CONTOUR)
        return self


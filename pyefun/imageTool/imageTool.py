import base64

import cv2
import numpy as np

from PIL import Image, ImageDraw, ImageFont


class 图像操作类(object):
    """
    本类用于图像操作 使用cv2封装的类
    """

    def __init__(self, obj=None):
        """
        图像操作类初始化

        :param obj 可以是图像路径，图像字节集，图像base64
        """
        # print(type(obj))
        if type(obj) == str:
            self.img = cv2.imread(obj)
        else:
            self.img = obj

    # 创建空白图片
    def 创建空白图片(self, 宽度, 高度, 颜色=(255, 255, 255)):
        self.img = np.zeros((宽度, 高度, 3), np.uint8)
        self.img[:] = [颜色[2], 颜色[1], 颜色[0]]
        return self

    def 加载图片从文件(self, img_path):
        # 从文件中加载cv2对象
        data = np.fromfile(img_path, dtype=np.uint8)
        self.img = cv2.imdecode(data, cv2.IMREAD_ANYCOLOR)
        return self

    def 加载图片从字节集(self, img_bytes):
        # 从字节集中加载cv2对象
        data = np.frombuffer(img_bytes, np.uint8)
        self.img = cv2.imdecode(data, cv2.IMREAD_ANYCOLOR)
        return self

    def 加载图片从base64(self, img_bytes):
        img_bytes = base64.b64decode(img_bytes)
        img_array = np.frombuffer(img_bytes, np.uint8)
        self.img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return self

    def 加载图片从PIL(self, image):
        self.img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        return self

    # 图片转换为base64
    def 到base64(self):
        _, img_encode = cv2.imencode('.jpg', self.img)
        base64_str = base64.b64encode(img_encode.tobytes())
        return base64_str

    def 到PIL(self):
        return Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))

    @property
    def 宽度(self):
        return self.img.shape[1]

    @property
    def 高度(self):
        return self.img.shape[0]

    # 图片缩放
    def 缩放(self, scale=0.5):
        """
        图片操作.缩放(scale).显示图片()   scale为缩放比例 0.5为缩小一倍，2为放大一倍
        :param scale: 缩放比例
        :return:
        """
        self.img = cv2.resize(self.img, (int(self.img.shape[1] * scale), int(self.img.shape[0] * scale)))
        return self

    def 图像翻转左右(self):
        # flipCode 参数为-1.0,1,2 分别表示对角翻转,水平翻转，垂直翻转
        img = cv2.flip(self.img, 1)
        return 图像操作类(img)

    def 图像翻转上下(self):
        img = cv2.flip(self.img, 0)
        return 图像操作类(img)

    # 取某点颜色值
    def 取颜色(self, x, y):
        return self.img[y, x]

    # 绘制点
    def 绘制点(self, x, y, color=(0, 0, 255), 粗细=1):
        color = (color[2], color[1], color[0])
        cv2.circle(self.img, (x, y), 1, color, 粗细)
        return self

    def 剪裁(self, x1, y1, x2, y2):
        if (0 > x1):
            x1 = 0
        if (0 > y1):
            y1 = 0
        if (self.宽度 < x2):
            x2 = self.宽度
        if (self.高度 < y2):
            y2 = self.高度
        if x2 < x1:
            raise IndexError("尺寸不对")
        if y2 < y1:
            raise IndexError("尺寸不对")

        return 图像操作类(self.img[y1:y2, x1:x2])

    def 保存为文件(self, path=None):
        cv2.imwrite(path, self.img)
        return self

    def 到字节集(self):
        return cv2.imencode('.png', self.img)[1].tobytes()

    def 显示图片(self):
        """
        图片操作.显示图片()
        :return: -1为关闭了窗口 其他为键代码 可以使用 ord('1') 获取键代码
        """
        cv2.imshow("show", self.img)
        cv2.moveWindow("show" , 0, 0)
        on = cv2.waitKey(0)
        cv2.destroyAllWindows()
        return on

    # 图片二值化
    def 二值化(self, threshold=127):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        return 图像操作类(binary)

    def 二值化自动(self):
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY);
        # # 二值化
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 27, 28)

        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
        img = cv2.filter2D(img, -1, kernel=kernel)

        return 图像操作类(img)

    # 黑白颜色翻转
    def 颜色翻转(self):
        return 图像操作类(cv2.bitwise_not(self.img))

    def 绘制多边形(self, points, color=(255, 0, 0), 粗细=2):
        color = (color[2], color[1], color[0])
        cv2.polylines(self.img, [np.array(points, dtype=np.int32)], True, color, 粗细)
        return self

    def 绘制矩形(self, x1, y1, x2, y2, color=(255, 0, 0), thickness=1):
        color = (color[2], color[1], color[0])
        cv2.rectangle(self.img, (x1, y1), (x2, y2), color, thickness)
        return self

    def 绘制文本(self, text, x, y, font=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=1):
        cv2.putText(self.img, text, (x, y), font, fontScale, color, thickness)
        return self

    def 绘制文本汉字(self, text, x, y, color=(255, 0, 0), font_size=30):
        img = self.到PIL()
        draw = ImageDraw.Draw(img)
        fontStyle = ImageFont.truetype("msyh.ttc", font_size, encoding="utf-8")
        draw.text((x, y), text, color, font=fontStyle)
        self.img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        return self

    def 绘制填充矩形(self, x1, y1, x2, y2, color=(255, 0, 0), transparency=0.5):
        blk = np.zeros(self.img.shape, np.uint8)
        cv2.rectangle(blk, (x1, y1), (x2, y2), color, -1)
        blk = cv2.cvtColor(blk, cv2.COLOR_RGB2BGR)
        self.img = cv2.addWeighted(self.img, 1.0, blk, transparency, 1)
        return self

    def 绘制填充多边形(self, points, color=(255, 0, 0), transparency=0.5):
        blk = np.zeros(self.img.shape, np.uint8)
        cv2.fillPoly(blk, [np.array(points, dtype=np.int32)], color)
        blk = cv2.cvtColor(blk, cv2.COLOR_RGB2BGR)
        self.img = cv2.addWeighted(self.img, 1.0, blk, transparency, 1)
        return self

"""
用于飞浆的分类模型 onnx 推理

需要安装 onnxruntime

"""

import time
import cv2
import numpy as np
import onnxruntime
from pyefun import *


def 输入图像预处理(输入数据):
    # 将输入数据转换为浮动32输入
    图像数据 = 输入数据.astype('float32')
    # 图像均值
    图像均值 = np.array([0.485, 0.456, 0.406])
    # 图像方差
    图像方差 = np.array([0.229, 0.224, 0.225])

    # 获得图像的矩阵用0填充
    标准图像数据 = np.zeros(图像数据.shape).astype('float32')
    # 图像归一化
    for i in range(图像数据.shape[0]):
        标准图像数据[i, :, :] = (图像数据[i, :, :] / 255 - 图像均值[i]) / 图像方差[i]

    # 添加输入通道
    标准图像数据 = 标准图像数据.reshape(1, 3, 224, 224).astype('float32')
    return 标准图像数据


def softmax(x):
    x = x.reshape(-1)
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


def 加载标签数据(标签文件路径):
    return 读入文本(标签文件路径).rstrip('\n').split('\n')


class 分类模型:
    def __init__(self, 模型文件路径, 标签文件路径=""):
        try:
            self.标签数据 = 读入文本(标签文件路径).rstrip('\n').split('\n')
        except:
            self.标签数据 = []
        self.模型 = onnxruntime.InferenceSession(模型文件路径)

    def 预测(self, 图片路径):
        图像 = cv2.imread(图片路径)
        # bgr 数据 转换为 rgb数据
        图像 = cv2.cvtColor(图像, cv2.COLOR_BGR2RGB)
        # 重置图像大小
        图像 = cv2.resize(图像, (224, 224))  # shape (224, 224, 3)  对应轴0 1 2
        图像数据 = np.array(图像).transpose(2, 0, 1)  # shape (3, 224, 224) 对应轴 2 1 0
        输入数据图像 = 输入图像预处理(图像数据)
        输出数据 = self.模型.run(output_names=None, input_feed={'image': 输入数据图像})
        self.result = softmax(np.array(输出数据)).tolist()
        idx = np.argmax(self.result)
        try:
            标签文本 = self.标签数据[idx]
        except:
            pass
            标签文本 = ""
        return idx, 标签文本

    def 取top1(self):
        return np.argmax(self.result)

    def 取top5(self):
        """前5预测结果"""
        sort_idx = np.flip(np.argsort(self.result))
        # print(分类标签[sort_idx[:5]])
        lable = []
        for k in sort_idx[:5]:
            try:
                lable.append(self.标签数据[k])
            except:
                pass
        return sort_idx[:5], lable


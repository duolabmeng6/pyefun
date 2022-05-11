import unittest

import pyefun.ai.ONNXClassInference as onnx


class TestONNXInference(unittest.TestCase):

    def test_1(self):
        pass

        ONNX分类模型 = onnx.分类模型(
            模型文件路径="./狗狗品种分类模型/onnx/onnx_file",
            # 标签文件路径="./狗狗品种分类模型/onnx/labels.txt"
        )
        标签索引,标签文本 = ONNX分类模型.预测(图片路径="./Alaskan_malamute_00346.jpg")
        print(标签索引,标签文本)
        print(ONNX分类模型.取top1(),ONNX分类模型.取top5())


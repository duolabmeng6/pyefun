"""
需要安装 ppppocr 的库
pip install ppppocr
"""
import ppppocr

ocr = ppppocr.ppppOcr()


def 通用文字识别(图片路径):
    dt_boxes, rec_res = ocr.ocr(图片路径)
    return dt_boxes, rec_res


def 通用文字识别获取文字(图片路径):
    dt_boxes, rec_res = ocr.ocr(图片路径)
    return ocr.toText(rec_res)


def 通用文字识别获取Json(图片路径):
    dt_boxes, rec_res = ocr.ocr(图片路径)
    return ocr.toJson(dt_boxes, rec_res)

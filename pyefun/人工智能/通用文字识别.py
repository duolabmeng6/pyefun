"""
需要安装 rapidocr 的库
pip install rapidocr-onnxruntime
"""


def 通用文字识别(图片路径):
    rapid_ocr = RapidOCR()
    return result


def 通用文字识别获取文字(图片路径):
    rapid_ocr = RapidOCR()
    result = rapid_ocr(图片路径)
    results = []
    for i, (rec, text, score) in enumerate(result[0]):
        results.append(text)
        print(text)
    return " ".join(results)


def 通用文字识别获取Json(图片路径):
    rapid_ocr = RapidOCR()
    result = rapid_ocr(图片路径)
    results = []
    for i, (dt_boxes, text, score) in enumerate(result[0]):
        results.append(text)
        print(text)
        boxs = [(int(v[0]), int(v[1])) for v in dt_boxes]
        results.append({
            "text_box_position": boxs,
            "text": text,
            "confidence": str(score),
        })
    return results
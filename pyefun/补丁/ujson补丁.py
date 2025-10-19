"""
直接把 json 对象替换为 ujson
"""
import json
import ujson


def 补丁json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads


补丁json()

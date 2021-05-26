import urllib.parse


def url编码(欲编码的文本, encoding="utf-8"):
    """
    encoding 可以设置为 gbk
    """
    return urllib.parse.quote(欲编码的文本, encoding=encoding)


def url解码(url,encoding="utf-8"):
    """
    encoding 可以设置为 gbk
    """
    return urllib.parse.unquote(url, encoding=encoding)

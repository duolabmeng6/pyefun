import gzip


def gzip压缩(data, 压缩级别=9):
    """
    压缩级别 1-9 9是最高压缩级别
    """
    return gzip.compress(data, 压缩级别)


def gzip解压(data):
    return gzip.decompress(data)

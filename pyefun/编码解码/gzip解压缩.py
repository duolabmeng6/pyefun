import gzip


def gzip压缩(data, 压缩级别=9):
    """
    压缩级别 1-9 9是最高压缩级别
    """
    return gzip.compress(data, 压缩级别)


def gzip解压(data):
    """
    gzip解压 的功能说明（请补充）。

    Args:
        data: 参数说明。

    """
    return gzip.decompress(data)

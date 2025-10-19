import binascii

def binary编码(data):
    """
    binary编码 的功能说明（请补充）。

    Args:
        data: 参数说明。

    """
    if (type(data) == str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data
    return binascii.b2a_hex(data_bytes)


def binary解码(data):
    """
    binary解码 的功能说明（请补充）。

    Args:
        data: 参数说明。

    """
    return binascii.a2b_hex(data)

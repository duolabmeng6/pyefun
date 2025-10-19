"""
剪切板操作

pip install pyperclip

"""
import pyperclip

def 取剪辑板文本() -> str:
    """
    取剪辑板文本 的功能说明（请补充）。

    Returns:
        str: 返回值说明。

    """
    return pyperclip.paste()


def 置剪辑板文本(str):
    """
    置剪辑板文本 的功能说明（请补充）。

    Args:
        str: 参数说明。

    """
    pyperclip.copy(str)


def 剪辑板中可有文本() -> bool:
    """
    剪辑板中可有文本 的功能说明（请补充）。

    Returns:
        bool: 返回值说明。

    """
    return 取剪辑板文本() != ""


def 清除剪辑板():
    """
    清除剪辑板 的功能说明（请补充）。

    """
    pyperclip.copy("")
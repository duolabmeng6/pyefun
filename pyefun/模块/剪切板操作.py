"""
剪切板操作

pip install pyperclip

"""
import pyperclip

def 取剪辑板文本() -> str:
    return pyperclip.paste()


def 置剪辑板文本(str):
    pyperclip.copy(str)


def 剪辑板中可有文本() -> bool:
    return 取剪辑板文本() != ""


def 清除剪辑板():
    pyperclip.copy("")
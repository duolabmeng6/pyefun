from pyefun import *
# 朗读声音
# 需要安装
# pip install pyttsx3
import multiprocessing
import pyttsx3
import time
from threading import Thread

# 创建 TTS 引擎对象
if 系统_是否为window系统():
    import pyttsx3

    engine = pyttsx3.init()
else:
    from pyefun.模块.苹果系统操作 import *


def threaded(fn):
    """
    threaded 的功能说明（请补充）。

    Args:
        fn: 参数说明。

    """
    def wrapper(*args, **kwargs):
        """
        wrapper 的功能说明（请补充）。

        Args:
            *args: 参数说明。
            **kwargs: 参数说明。

        """
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def speak(phrase):
    """
    speak 的功能说明（请补充）。

    Args:
        phrase: 参数说明。

    """
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()


def stop_speaker():
    """
    stop_speaker 的功能说明（请补充）。

    """
    global term
    term = True
    t.join()


@threaded
def manage_process(p):
    """
    manage_process 的功能说明（请补充）。

    Args:
        p: 参数说明。

    """
    global term
    while p.is_alive():
        if term:
            p.terminate()
            term = False
        else:
            continue


def 朗读(phrase):
    """
    朗读 的功能说明（请补充）。

    Args:
        phrase: 参数说明。

    """
    if 系统_是否为window系统():
        global t
        global term
        term = False
        p = multiprocessing.Process(target=speak, args=(phrase,))
        p.start()
        t = manage_process(p)

    if 系统_是否为mac系统():
        文本朗读(phrase)


if __name__ == '__main__':
    朗读("你好，世界")
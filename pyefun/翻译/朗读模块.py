from pyefun import *
# 朗读声音
# 需要安装
# pip install pyttsx3

engine = None
# 创建 TTS 引擎对象
if 系统_是否为window系统():
    import pyttsx3
    engine = pyttsx3.init()
else:
    from pyefun.模块.苹果系统操作 import *



def 朗读(文字):
    global engine
    if 系统_是否为window系统():
        engine.stop()
        engine.say(文字)
        engine.runAndWait()

    if 系统_是否为mac系统():
        文本朗读(文字)
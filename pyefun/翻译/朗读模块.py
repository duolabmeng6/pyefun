# 朗读声音
# 需要安装
# pip install pyttsx3

import pyttsx3

# 创建 TTS 引擎对象
engine = pyttsx3.init()


def 朗读(文字):
    engine.say(文字)
    engine.runAndWait()

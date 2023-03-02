# 朗读声音
# 需要安装
# pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()



def 朗读(文字):
    # 创建 TTS 引擎对象
    engine.say(文字)
    engine.runAndWait()

if __name__ == '__main__':
    朗读("你好，世界")
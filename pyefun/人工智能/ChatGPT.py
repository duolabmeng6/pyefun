import openai
from pyefun import *
from pyefun.调试 import *

def 聊天机器人(api_key, 聊天内容):
    openai.api_key = api_key
    # model_engine = "text-davinci-003"
    model_engine = "text-davinci-003"
    # engine_name = "davinci-codex"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=聊天内容,
        max_tokens=512,
        temperature=0.9,
        n=1,
        stop=None,
    )
    print(response)
    message = response.choices[0].text.strip()
    return message


class 机器人连续聊天:
    def __init__(self, api_key):
        self.api_key = api_key
        # self.聊天内容 = "以下是与AI助手的对话。助手乐于助人，富有创造力，聪明且非常友好."
        self.聊天内容 = "以下是与AI助手的对话。"
        self.问答列表 = []
        self.问答列表.append(self.聊天内容 + "\n\n")
        self.max_tokens = 512
        self.问答轮数 = 10
    def 清空对话(self):
        self.问答列表 = []
        self.问答列表.append(self.聊天内容 + "\n\n")


    def _获取机器人回答(self, 内容):

        # return 文本_取随机数字(1)
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=内容,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print(response)
        message = response.choices[0].text.strip()
        return message

    def 发送消息(self, 问题):
        现在新的内容 = "Human: " + 问题 + "\nAI:"
        self.问答列表.append(现在新的内容)
        prompt = "".join(self.问答列表)

        # 处理超出长度的问题
        for i in range(3):
            if len(prompt) >= self.max_tokens:
                self.问答列表.pop(0)
                prompt = "".join(self.问答列表)
        # 减掉一个回答还是超出就直接减掉
        if len(prompt) >= self.max_tokens:
            prompt = prompt[-self.max_tokens:]

        # print("------",len(self.问答列表)-1)
        # print(prompt)
        try:
            机器人回答 = self._获取机器人回答(prompt)
        except:
            机器人回答 = "机器人回答失败"


        last_index = len(self.问答列表) - 1
        self.问答列表[last_index] += 机器人回答 + "\n"

        if len(self.问答列表) >= self.问答轮数:
            self.问答列表 = self.问答列表[-self.问答轮数:]
        print("回答后------",len(self.问答列表)-1)
        prompt = "".join(self.问答列表)
        print(prompt)

        return 机器人回答



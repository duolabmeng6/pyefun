# 用于操作钉钉机器人的模块
# 需要安装模块pip install DingtalkChatbot
# 使用教程 https://github.com/zhuifengshen/DingtalkChatbot
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem



class 钉钉机器人:
    def __init__(self, webhook, secret=""):
        self.机器人 = ""
        if secret is "":
            self.机器人 = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
        else:
            self.机器人 = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

    def 发送文本消息(self, 消息内容):
        self.机器人.send_text(msg=消息内容)

    def 发送链接消息(self, 消息内容, 消息标题, 消息URL, 消息图片URL):
        # # Link消息
        self.机器人.send_link(title=消息标题, text=消息内容, message_url=消息URL, pic_url=消息图片URL)


    def 发送markdown消息(self, 消息内容):
        self.机器人.send_markdown(title="markdown", text=消息内容)

    def 发送图片消息(self, 图片网络地址):
        self.机器人.send_image(图片网络地址)

    def 整体跳转消息类型(self, 消息标题, 消息内容, 消息URL):
        按钮组 = [CardItem(title="查看详情", url=消息URL)]
        卡片 = ActionCard(title=消息标题,
                                    text=消息内容,
                                    btns=按钮组,
                                    btn_orientation=1,
                                    hide_avatar=1)
        self.机器人.send_action_card(卡片)






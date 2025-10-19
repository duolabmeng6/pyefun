# 用于操作钉钉机器人的模块
# 需要安装模块pip install DingtalkChatbot
# 使用教程 https://github.com/zhuifengshen/DingtalkChatbot
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem



class 钉钉机器人:
    def __init__(self, webhook, secret=""):
        """
        __init__ 的功能说明（请补充）。

        Args:
            webhook: 参数说明。
            secret (可选): 参数说明。默认值为 ""。

        """
        self.机器人 = ""
        if secret is "":
            self.机器人 = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
        else:
            self.机器人 = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

    def 发送文本消息(self, 消息内容):
        """
        发送文本消息 的功能说明（请补充）。

        Args:
            消息内容: 参数说明。

        """
        self.机器人.send_text(msg=消息内容)

    def 发送链接消息(self, 消息内容, 消息标题, 消息URL, 消息图片URL):
        # # Link消息
        """
        发送链接消息 的功能说明（请补充）。

        Args:
            消息内容: 参数说明。
            消息标题: 参数说明。
            消息URL: 参数说明。
            消息图片URL: 参数说明。

        """
        self.机器人.send_link(title=消息标题, text=消息内容, message_url=消息URL, pic_url=消息图片URL)


    def 发送markdown消息(self, 消息内容):
        """
        发送markdown消息 的功能说明（请补充）。

        Args:
            消息内容: 参数说明。

        """
        self.机器人.send_markdown(title="markdown", text=消息内容)

    def 发送图片消息(self, 图片网络地址):
        """
        发送图片消息 的功能说明（请补充）。

        Args:
            图片网络地址: 参数说明。

        """
        self.机器人.send_image(图片网络地址)

    def 整体跳转消息类型(self, 消息标题, 消息内容, 消息URL):
        """
        整体跳转消息类型 的功能说明（请补充）。

        Args:
            消息标题: 参数说明。
            消息内容: 参数说明。
            消息URL: 参数说明。

        """
        按钮组 = [CardItem(title="查看详情", url=消息URL)]
        卡片 = ActionCard(title=消息标题,
                                    text=消息内容,
                                    btns=按钮组,
                                    btn_orientation=1,
                                    hide_avatar=1)
        self.机器人.send_action_card(卡片)






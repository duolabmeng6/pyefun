"""
发送邮件

https://github.com/zhangyunhao116/zmail

pip install zmail
"""
import zmail

def 发送邮件(邮箱,密码,收件邮箱,标题,内容,是否HTML=False):
    '成功返回True 失败返回False'
    if 是否HTML:
        mail = {'subject': 标题,'content_html': 内容}
    else:
        mail = {'subject': 标题,'content_text': 内容}
    try:
        server = zmail.server(邮箱, 密码)
        server.send_mail(收件邮箱, mail, timeout=15)
        return True
    except Exception as e:
        print(e)
        return False
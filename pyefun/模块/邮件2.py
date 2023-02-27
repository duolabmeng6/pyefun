import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def 发送QQ邮箱(发送邮箱号, 接收邮箱号, 授权码, 邮件标题, 邮件内容='', 邮件内容类型='plain', 附件文件=None):
    """
    发送邮件函数

    :param 发送邮箱号: 发送邮箱号
    :param 接收邮箱号:  接收邮箱号
    :param 授权码: 授权码，登录qq邮箱-设置-账户-pop3/smtp开启，获取授权码
    :param 邮件标题: 邮件标题
    :param 邮件内容: 邮件内容
    :param 邮件内容类型: 邮件内容类型，普通：plain，富文本：html
    :param 附件文件: 附件名称
    :return:
    """
    # 创建邮件对象，并设置标题、发送人、收件人、邮件内容等信息
    message = MIMEMultipart()
    # 邮件标题
    message['Subject'] = Header(邮件标题, 'utf-8')
    message['From'] = 发送邮箱号
    message['To'] = 接收邮箱号
    # 邮件正文
    message.attach(MIMEText(邮件内容.encode('utf-8'), 邮件内容类型, 'utf-8'))

    # 添加附件
    if 附件文件:
        filename = os.path.basename(附件文件)
        mime = MIMEBase('application', 'octet-stream')
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        # 附件内容
        with open(附件文件, 'rb') as f:
            mime.set_payload(f.read())
        # Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart
        message.attach(mime)

    # 设置服务器地址和端口号
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.set_debuglevel(1)
    # 登录邮箱号和对应的授权码
    smtp.login(发送邮箱号, 授权码)
    # 发送邮箱号和接收邮箱号
    smtp.sendmail(发送邮箱号, 接收邮箱号, message.as_string())
    smtp.quit()


if __name__ == '__main__':
    msg = '''
    pyefun发送邮件测试
    '''
    发送邮件(发送邮箱号="发送邮箱地址@qq.com",
         接收邮箱号='接受邮件地址@qq.com',
         授权码="授权码",
         邮件标题='pyefun发送邮件测试',
         邮件内容=msg)

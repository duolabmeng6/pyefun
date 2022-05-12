"""

.. Hint::
    正则表达式


.. literalinclude:: ../../../pyefun/正则表达式实用函数_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
import re


# 正则匹配数字
def 正则匹配数字(数字):
    return re.match(r'^[0-9]*$', 数字).string


# 正则表达式匹配英文
def 正则匹配英文(英文):
    pattern = re.compile(r'[a-zA-Z]')
    return pattern.match(英文).string


# 正则表达式匹配手机号码
def 正则匹配中文(中文):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    return pattern.match(中文).string


# 正则表达式匹配手机号码
def 正则匹配手机号码(手机号):
    """
    正则表达式匹配手机号码
    :param 手机号:
    :return:
    """
    pattern = re.compile(r'^1[3-9]\d{9}$')
    return pattern.match(手机号).string


# 正则表达式匹配邮箱
def 正则匹配邮箱(邮箱):
    """
    正则表达式匹配邮箱
    :param 邮箱:
    :return:
    """
    pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
    return pattern.match(邮箱).string


# 正则表达式匹配身份证号码
def 正则匹配身份证号码(身份证号码):
    """
    正则表达式匹配身份证号码
    :param 身份证号码:
    :return:
    """
    pattern = re.compile(r'^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$')
    return pattern.match(身份证号码).string


# 正则表达式匹配银行卡号
def 正则匹配银行卡号(银行卡号):
    """
    正则表达式匹配银行卡号
    :param 银行卡号:
    :return:
    """
    pattern = re.compile(r'^[1-9]\d{9,22}$')
    return pattern.match(银行卡号).string


# 正则表达式匹配邮政编码
def 正则匹配邮政编码(邮政编码):
    """
    正则表达式匹配邮政编码
    :param 邮政编码:
    :return:
    """
    pattern = re.compile(r'^[1-9]\d{5}$')
    return pattern.match(邮政编码).string


# 正则表达式匹配IP地址
def 正则匹配IP地址(IP地址):
    """
    正则表达式匹配IP地址
    :param IP地址:
    :return:
    """
    pattern = re.compile(r'^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$')
    return pattern.match(IP地址).string


# 正则表达式匹配URL
def 正则匹配URL(URL):
    """
    正则表达式匹配URL
    :param URL:
    :return:
    """
    pattern = re.compile(r'^[a-zA-z]+://[^\s]*$')
    return pattern.match(URL).string


# 正则表达式匹配用户名
def 正则匹配用户名(用户名):
    """
    正则表达式匹配用户名
    :param 用户名:
    :return:
    """
    pattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')
    return pattern.match(用户名).string


# 正则表达式匹配密码
def 正则匹配密码(密码):
    """
    正则表达式匹配密码
    :param 密码:
    :return:
    """
    pattern = re.compile(r'^[a-zA-Z0-9_]{6,20}$')
    return pattern.match(密码).string

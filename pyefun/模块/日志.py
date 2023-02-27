import logging
from logging import handlers

# 日志级别字典
__level_dict = {
    'critical': logging.CRITICAL,
    'fatal': logging.CRITICAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'warn': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}


def 创建日志类(日志文件路径=None, 显示级别='info', 日志分割时间单位='D', 备份个数=3,
          fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
    """
    获取日志处理对象

    :param 日志文件路径: 日志文件名称
    :param 显示级别: 日志等级：debug, info, warn/warning, error, critical
    :param 日志分割时间单位: 日志文件分割的时间单位，单位有以下几种:<br>
                - S 秒<br>
                - M 分<br>
                - H 小时<br>
                - D 天<br>
                - W 每星期<br>
                - midnight 每天凌晨<br>
    :param 备份个数: 备份文件的个数，如果超过这个数量，就会自动删除
    :param fmt: 日志信息格式
    :return:
    """
    显示级别 = __level_dict.get(显示级别.lower(), None)
    logger = logging.getLogger(日志文件路径)
    # 设置日志格式
    format_str = logging.Formatter(fmt)
    # 设置日志级别
    logger.setLevel(显示级别)
    # 控制台输出
    console_handler = logging.StreamHandler()
    # 控制台输出的格式
    console_handler.setFormatter(format_str)
    logger.addHandler(console_handler)

    if 日志文件路径:
        # 文件输出
        file_handler = handlers.TimedRotatingFileHandler(filename=日志文件路径, when=日志分割时间单位, backupCount=备份个数,
                                                         encoding='utf-8')

        # 文件输出的格式
        file_handler.setFormatter(format_str)
        logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    # log = 创建日志类('test.log')
    log = 创建日志类(None)
    log.debug('debug')
    log.info('info')
    log.warning('警告')
    log.error('报错')
    log.critical('严重')
    # 创建日志类('error.log', level='error').error('error')

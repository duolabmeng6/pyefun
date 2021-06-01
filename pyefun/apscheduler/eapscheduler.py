"""
定时任务

需要安装第三方模块

pip install apscheduler


"""

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

def 时钟_循环间隔模式(后台模式=False, 子程序=None, 元组参数=None, 字典参数=None, 序号=None, weeks周=0, days天=0, hours小时=0,
              minutes分钟=0, seconds秒钟=0, 开始时间='2020-01-01 00:00:01', 结束时间=None, 延时执行=None, 同时允许的线程数=0):
    """

    设置最大同时允许线程数可以解决 程序本身允许时间超过循环的时间,
    例子,scheduler .add_job(job_func, 'interval', minutes=2, start_date='2019-04-15 17:00:00' , end_date='2019-12-31 24:00:00')

    """
    if 同时允许的线程数 == 0:
        if 后台模式 == False:
            scheduler = BlockingScheduler()
        else:
            scheduler = BackgroundScheduler()
    else:
        job_defaults = {'max_instances': 同时允许的线程数}
        if 后台模式 == False:
            scheduler = BlockingScheduler(job_defaults=job_defaults)
        else:
            scheduler = BackgroundScheduler(job_defaults=job_defaults)
    scheduler.add_job(func=子程序, trigger='interval', args=元组参数, kwargs=字典参数, id=序号, weeks=weeks周, days=days天,
                      hours=hours小时,
                      minutes=minutes分钟, seconds=seconds秒钟, start_date=开始时间, end_date=结束时间, jitter=延时执行)
    scheduler.start()

def 时钟_一次性运行(后台模式=False, 子程序=None, 元组参数=None, 字典参数=None, 序号=None, datetime运行的日期=None, 同时允许的线程数=0):
    """

    设置最大同时允许线程数可以解决 程序本身允许时间超过循环的时间,
    运行时间可以是datetime 或 文本型时间 scheduler.add_job(my_job, 'date', run_date='2009-11-06 16:30:05', args=['测试任务'])

    """
    if 同时允许的线程数 == 0:
        if 后台模式 == False:
            scheduler = BlockingScheduler()
        else:
            scheduler = BackgroundScheduler()
    else:
        job_defaults = {'max_instances': 同时允许的线程数}
        if 后台模式 == False:
            scheduler = BlockingScheduler(job_defaults=job_defaults)
        else:
            scheduler = BackgroundScheduler(job_defaults=job_defaults)
    scheduler.add_job(func=子程序, trigger='date', args=元组参数, kwargs=字典参数, id=序号, run_date=datetime运行的日期)
    scheduler.start()

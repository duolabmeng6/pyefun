# -*- coding:utf-8 -*-
import pymysql,re
from .public import *

#事务回滚等操作需要支持库使用INNODB引擎

@异常处理返回类型逻辑型
def 连接Mysql(连接地址, 用户名, 密码, 数据库名, 端口号,自动提交=True, 编码='utf8'):
    '成功返回连接对象,开启 自动提交 后不能使用保留点操作'
    db = pymysql.connect(host=连接地址, port=int(端口号), user=用户名, passwd=密码, db=数据库名, charset=编码,autocommit=自动提交)
    if db:
        return 数据库类(db)
    return False



class 游标类:
    def __init__(self,游标对象):
        '传入连接Mysql后通过cursor获取的游标'
        self.__cursor = 游标对象

    @异常处理返回类型逻辑型
    def 关闭游标(self):
        self.__cursor.close()
        return True

    @异常处理返回类型逻辑型
    def 取全部记录(self):
        '一次读取全部数据，如果管道内没有数据，则返回空元组或空列表'
        return self.__cursor.fetchall()

    @异常处理返回类型逻辑型
    def 取下一条记录(self):
        '一次一条数据'
        return self.__cursor.fetchone()

    @异常处理返回类型逻辑型
    def 取多条记录(self,数量=1):
        '一次多条数据，括号内填入要读取的数据条数。不填则为1条数据，如果读数超过实际条数，只显示实际条数'
        return self.__cursor.fetchmany(数量)

    @异常处理返回类型逻辑型
    def 移到指定位置(self, 位置):
        '首位为0。（第0位为第一条数据）'
        return self.__cursor.scroll(位置,mode='absolute')

    @异常处理返回类型逻辑型
    def 移到相对位置(self, 位置):
        '例：传入3则表示移到当前位置往后第三条记录的位置上'
        return self.__cursor.scroll(位置, mode='relative')

    @异常处理返回类型逻辑型
    def 取当前指针位置(self):
        '上次光标位置'
        return self.__cursor.lastrowid

    @异常处理返回类型逻辑型
    def 执行SQL语句(self,sql):
        '返回受影响的行数'
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 增加记录_批量(self,表名,字段名列表,数据列表):
        '''
        用于增加多条记录等操作，效率比execute快很多
        :param 表名: user
        :param 字段名列表: ['user','pwd']
        :param 数据列表: [('123456','a11111'),('56789','aaaaa1')]
        :return: 返回受影响的行数
        '''
        字段 = "`{}`".format("`,`".join(字段名列表))
        sql = "insert into `{}` ({}) value ({})".format(表名,字段,('%s,'*len(字段名列表))[:-1])
        return self.__cursor.executemany(sql,数据列表)

    @异常处理返回类型逻辑型
    def 增加记录(self, 表名, 字段名列表, 数据列表):
        '''
        :param 表名: user
        :param 字段名列表: ['user','pwd']
        :param 数据列表: [('123456','a11111'),('56789','aaaaa1')]
        :return: 返回受影响的行数
        '''
        字段 = "`{}`".format("`,`".join(字段名列表))
        sql = "insert into `{}` ({}) value {}".format(表名, 字段, repr(数据列表)[1:-1])
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 追加内容(self, 表名, 字段名, 加入的内容,加入位置=0,条件=''):
        '加入位置:0.前面 1.后面   条件可空，空为全部操作'
        条件 += ' where ' if 条件 else ''
        if 加入位置:
            sql = "update {} set {} = concat({},{}){};".format(表名,字段名,字段名,加入的内容,条件)
        else:
            sql = "update {} set {} = concat({},{}){};".format(表名,字段名,加入的内容,字段名,条件)
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 查找记录_按时间范围(self, 表名,字段名,开始时间,结束时间,时间格式='%Y-%m-%d %H:%M:%S'):
        sql = "select * from {} where from_unixtime({},'{}') between '{}' and '{}';".format(表名,字段名,时间格式,开始时间,结束时间)
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 查找记录_指定日期(self, 表名,字段名,日期,时间格式='%Y-%m-%d %H:%M:%S'):
        sql = "select * from {} where from_unixtime({},'{}') = '{}'".format(表名,字段名,时间格式,日期)
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 查找记录_取记录数(self, 表名, 查找条件='', 模糊查找=False):
        '''
        :param 表名: 表名
        :param 查找条件: id='123' and user='456'
        :param 模糊查找:
        :return: 返回记录条数
        '''
        if 模糊查找:
            z = re.findall("='.*?'", 查找条件)
            for x in z:
                查找条件 = 查找条件.replace(x, x[:-1].replace("='", " like '%") + "%'")
            sql = "select count(*) from {} where {}".format(表名, 查找条件)
        else:
            if 查找条件:
                sql = "select count(*) from {} where {}".format(表名, 查找条件)
            else:
                sql = "select count(*) from {}".format(表名)
        self.__cursor.execute(sql)
        return self.__cursor.fetchone()[0]

    @异常处理返回类型逻辑型
    def 查找记录(self, 表名, 字段名, 查找条件='',模糊查找=False, 取出的数量=0, 排序=""):
        '''
        :param 表名: 表名
        :param 字段名: id,user  需要返回的字段信息 * 为全部
        :param 查找条件: id='123' and user='456'
        :param 模糊查找:
        :param 取出的数量:
        :param 排序: id asc(根据ID字段正序排列)，id desc(根据ID字段倒序排列)
        :return: 返回受影响的行数
        '''
        if 模糊查找:
            z = re.findall("='.*?'", 查找条件)
            for x in z:
                查找条件 = 查找条件.replace(x, x[:-1].replace("='", " like '%") + "%'")
            sql = "select {} from {} where {}".format(字段名, 表名, 查找条件)
        else:
            if 查找条件:
                sql = "select {} from {} where {}".format(字段名,表名,查找条件)
            else:
                sql = "select {} from {}".format(字段名,表名)

        if 排序:
            sql += " order by " + 排序

        if 取出的数量:
            sql += " limit " + str(取出的数量)
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 更新记录(self, 表名, 更新条件, 更新内容,模糊匹配=False):
        if 模糊匹配:
            z = re.findall("='.*?'", 更新条件)
            for x in z:
                更新条件 = 更新条件.replace(x, x[:-1].replace("='", " like '%") + "%'")
            sql = "update {} set {} where {}".format(表名,更新内容,更新条件)
        else:
            sql = "update {} set {} where {}".format(表名,更新内容,更新条件)
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 删除记录(self, 表名, 删除条件, 模糊匹配=False):
        if 模糊匹配:
            z = re.findall("='.*?'", 删除条件)
            for x in z:
                删除条件 = 删除条件.replace(x,x[:-1].replace("='", " like '%")+"%'")
            sql = "delete from {} where {}".format(表名, 删除条件)
        else:
            sql = "delete from {} where {}".format(表名, 删除条件)
        return self.__cursor.execute(sql)

    @异常处理返回类型逻辑型
    def 取全部表名(self, 库名):
        '返回格式[表名,表名]'
        sql = "show tables from " + 库名
        self.__cursor.execute(sql)
        return [x[0] for x in self.__cursor.fetchall()]

    @异常处理返回类型逻辑型
    def 取全部字段名(self,表名,只取字段名=True):
        '默认返回格式[字段名,字段名...]'
        sql = "select * from " + 表名
        self.__cursor.execute(sql)
        if 只取字段名:
            return [x[0] for x in self.__cursor.description]
        else:
            return self.__cursor.description

    @异常处理返回类型逻辑型
    def 事务_开启(self):
        sql = "start transaction"
        self.__cursor.execute(sql)
        return True

    @异常处理返回类型逻辑型
    def 事务_设置保留点(self,保留点名称):
        sql = "savepoint " + 保留点名称
        self.__cursor.execute(sql)
        return True

    @异常处理返回类型逻辑型
    def 事务_保留点回滚(self, 保留点名称):
        sql = "rollback to " + 保留点名称
        self.__cursor.execute(sql)
        return True



class 数据库类:
    def __init__(self,连接对象):
        '传入连接Mysql后返回的对象'
        self.__dc = 连接对象

    @异常处理返回类型逻辑型
    def 获取游标(self,返回字典类型=False):
        '将取回值以字典形式显示,默认为False'
        if 返回字典类型:
            return 游标类(self.__dc.cursor(pymysql.cursors.DictCursor))
        else:
            return 游标类(self.__dc.cursor())


    @异常处理返回类型逻辑型
    def 断开连接(self):
        self.__dc.close()
        return True

    @异常处理返回类型逻辑型
    def 事务_提交(self):
        '执行成功返回True'
        self.__dc.commit()
        return True

    @异常处理返回类型逻辑型
    def 事务_回滚(self):
        '执行成功返回True'
        self.__dc.rollback()
        return True


    def 是否在线(self):
        '在线返回True'
        try:
            self.__dc.ping(reconnect=True)
            return True
        except:
            return False


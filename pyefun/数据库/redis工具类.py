# -*- coding: utf-8 -*-
# @Time : 2021-10-31 15:14
# @Author : LiGuangLong
import redis


class Redis:
    def __init__(self, localhost, port, db=0):
        """redis中默认16个数据库 默认使用第一个 每个库互相不干扰"""
        pool = redis.ConnectionPool(host=localhost, db=db, port=port, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)

    def 添加value(self, key, value, 过期时间秒=None, 过期时间毫秒=None, nx=None, xx=None):
        """
        在 Redis 中设置值，默认，不存在则创建，存在则修改
        nx - 如果设置为True，则只有name不存在时，当前set操作才执行
        xx - 如果设置为True，则只有name存在时，当前set操作才执行
        """
        return self.r.set(key, value, 过期时间秒, 过期时间毫秒, nx, xx)

    def 切片添加(self, key, 索引, value):
        return self.r.setrange(key, 索引, value)

    def 追加值(self, key, value):
        return self.r.append(key, value)

    def 自增value(self, key, 步长=1):
        """名称为key的string增1操作"""
        return self.r.incr(key, 步长)

    def 值增加(self, key, 增加值):
        """名称为key的string增加integer"""
        return self.r.incrby(key, 增加值)

    def 自减value(self, key, 步长=1):
        return self.r.decr(key, 步长)

    def 值减少(self, key, 减少值):
        return self.r.decrby(key, 减少值)

    def 获取value(self, key):
        return self.r.get(key)

    def 获取多个value(self, keys, *args):
        return self.r.mget(keys, *args)

    def 获取并修改(self, key, value):
        """设置新值并获取原来的值"""
        return self.r.getset(key, value)

    def 切片获取(self, key, start, end):
        return self.r.getrange(key, start, end)

    def key是否存在(self, key):
        """1存在 0 不存在"""
        return self.r.exists(key)

    def 获取key存在时间(self, key):
        return self.r.ttl(key)

    def 设置key存在时间(self, key, 时间):
        """单位秒"""
        return self.r.expire(key, 时间)

    def 移动key位置(self, key, dbindex数据库):
        return self.r.move(key, dbindex数据库)

    def 获取全部key(self):
        return self.r.keys()

    def 获取key数量(self):
        """返回当前数据库中key的数目"""
        return self.r.dbsize()

    def 删除(self, key):
        return self.r.delete(key)

    def 查看value类型(self, key):
        return self.r.type(key)

    def 清空当前库(self):
        return self.r.flushdb()

    def 清空全部数据(self):
        return self.r.flushall()

    def 切换数据库(self):
        return

    #####list操作 Redis的list类型其实就是一个每个子元素都是string类型的双向链表，链表的最大长度是2^32。list既可以用做栈，也可以用做队列。
    def list添加尾(self, key, *value):
        return self.r.rpush(key, *value)

    def list添加头(self, key, *value):
        return self.r.lpush(key, *value)

    def 获取list长度(self, key):
        return self.r.llen(key)

    def list获取(self, key, index=None, start=None, end=None):
        if index is not None:
            return self.r.lindex(key, index)
        elif start is not None and end is not None:
            return self.r.lrange(key, start, end)
        else:
            return self.r.lrange(key, 0, -1)

    def list下标赋值(self, key, index, value):
        """给名称为key的list中index位置的元素赋值"""
        return self.r.lset(key, index, value)

    def list删除多个value(self, key, 数量, value):
        """删除多个key的list中值为value的元素"""
        return self.r.lrem(key, 数量, value)

    def list删除首(self, key):
        """返回并删除名称为key的list中的首元素"""
        return self.r.lpop(key)

    def list删除尾(self, key):
        """：返回并删除名称为key的list中的尾元素"""
        return self.r.rpop(key)

    def list元素移动(self, srckey, dstkey):
        """返回并删除名称为srckey的list的尾元素，并将该元素添加到名称为dstkey的list的头部"""
        return self.r.rpoplpush(srckey, dstkey)

    ############################未封装完毕###############################32
    """
    Set
    特点：无序性、确定性、唯一性
    
    sadd(key, member)：向名称为key的set中添加元素member
    srem(key, member) ：删除名称为key的set中的元素member
    spop(key) ：随机返回并删除名称为key的set中一个元素
    smove(srckey, dstkey, member) ：移到集合元素
    scard(key) ：返回名称为key的set的基数
    sismember(key, member) ：member是否是名称为key的set的元素
    sinter(key1, key2,…key N) ：求交集
    sinterstore(dstkey, (keys)) ：求交集并将交集保存到dstkey的集合
    sunion(key1, (keys)) ：求并集
    sunionstore(dstkey, (keys)) ：求并集并将并集保存到dstkey的集合
    sdiff(key1, (keys)) ：求差集
    sdiffstore(dstkey, (keys)) ：求差集并将差集保存到dstkey的集合
    smembers(key) ：返回名称为key的set的所有元素
    srandmember(key) ：随机返回名称为key的set的一个元素
    Hash
    Redis hash 是一个string类型的field和value的映射表，它的添加、删除操作都是O(1)（平均）。hash特别适用于存储对象，将一个对象存储在hash类型中会占用更少的内存，并且可以方便的存取整个对象。
    
    hset(key, field, value)：向名称为key的hash中添加元素field
    hget(key, field)：返回名称为key的hash中field对应的value
    hmget(key, (fields))：返回名称为key的hash中field i对应的value
    hmset(key, (fields))：向名称为key的hash中添加元素field
    hincrby(key, field, integer)：将名称为key的hash中field的value增加integer
    hexists(key, field)：名称为key的hash中是否存在键为field的域
    hdel(key, field)：删除名称为key的hash中键为field的域
    hlen(key)：返回名称为key的hash中元素个数
    hkeys(key)：返回名称为key的hash中所有键
    hvals(key)：返回名称为key的hash中所有键对应的value
    hgetall(key)：返回名称为key的hash中所有的键（field）及其对应的value
    Zest
    概念：它是在set的基础上增加了一个顺序属性，这一属性在添加修改元素的时候可以指定，每次指定后，zset会自动按新的值调整顺序。可以理解为有两列的mysql表，一列存储value，一列存储顺序，操作中key理解为zset的名字。
    
    zadd key score1 value1：添加元素
    zrange key start stop [withscore]：把集合排序后,返回名次[start,stop]的元素 默认是升续排列 withscores 是把score也打印出来
    zrank key member：查询member的排名（升序0名开始）
    zrevrank key member：查询member排名（降序 0名开始）
    zrem key value1 value2：删除集合中的元素
    zremrangebyrank key start end：按排名删除元素，删除名次在[start, end]之间的
    zcard key：返回集合元素的个数
    zcount key min max：返回[min, max]区间内元素数量

    """


if __name__ == '__main__':
    r = Redis('121.43.149.217', 6379, 1)
    # print(r.清空全部数据())

    for i in r.获取全部key():
        print(f'{i}------{r.获取key存在时间(i)}')

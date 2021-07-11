"""

.. Hint::
    文本操作实用函数


.. literalinclude:: ../../../pyefun/stringUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
from .stringBase import *
import re
import random


def strCut(内容: str, 表达式: str) -> str:
    subbds = 表达式.split("$")
    if (len(subbds) == 2):
        return 文本_取出中间文本(内容, subbds[0], subbds[1])

    if (len(subbds) == 1):
        return 文本_取出中间文本(内容, subbds[0], "")
    return 内容


def 文本_取左边(需取文本: str, 欲寻找的文本: str) -> str:
    return 文本_取出中间文本(需取文本, "", 欲寻找的文本)


def 文本_取右边(需取文本: str, 欲寻找的文本: str) -> str:
    return 文本_取出中间文本(需取文本, 欲寻找的文本, "")


def 文本_取出中间文本(需取文本: str, 左边文本: str, 右边文本: str) -> str:
    leftLen = len(左边文本)
    try:
        leftP = 需取文本.index(左边文本)
    except:
        return ''
    if (leftP == -1):
        return ''
    if (右边文本 == ""):
        rigthP = len(需取文本) + 1
        leftP = leftP + leftLen
    else:
        leftP = leftP + leftLen
        try:
            rigthP = 需取文本.index(右边文本, leftP)
        except:
            return ''
        if (rigthP == - 1):
            return ''
    return 需取文本[leftP: rigthP]


def 文本_取随机字母(取出的数量: int, 类型: int = 2) -> str:
    '类型：0.小写 1.大写 2.混合'
    取出的数量 = 1 if 取出的数量 < 1 else 取出的数量
    类型 = 0 if 类型 < 0 or 类型 > 2 else 类型
    字母 = 'abcdefghijklnmopqrstuvwxyz'
    文本 = ''
    if 类型 == 0:
        for x in range(取出的数量):
            文本 += random.choice(字母)
    elif 类型 == 1:
        for x in range(取出的数量):
            文本 += random.choice(字母).upper()
    else:
        for x in range(取出的数量):
            随机数 = random.randint(0, 1)
            if 随机数 == 1:
                文本 += random.choice(字母)
            else:
                文本 += random.choice(字母).upper()
    return 文本


def 文本_取随机字母和数字(取出的数量: int) -> str:
    '包括0-9 a-z A-Z'
    取出的数量 = 1 if 取出的数量 < 1 else 取出的数量
    字符 = '0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ'
    文本 = ''
    for x in range(取出的数量):
        文本 += random.choice(字符)
    return 文本


def 文本_取随机数字(取出的数量: int) -> str:
    取出的数量 = 1 if 取出的数量 < 1 else 取出的数量
    字符 = '0123456789'
    文本 = ''
    for x in range(取出的数量):
        文本 += random.choice(字符)
    return 文本


def 文本_取随机汉字(取出的数量: int) -> str:
    '部分常见汉字'
    取出的数量 = 1 if 取出的数量 < 1 else 取出的数量
    文本 = ''
    部分汉字 = "的一是了我不人在他有这个上们来到时大地为子中你说生国年着就那和要她出也得里后自以会家可下而过天去能对小多然于心学么之都好看起发当没成只如事把还用第样道想作种开美总从无情己面最女但现前些所同日手又行意动方期它头经长儿回位分爱老因很给名法间斯知世什两次使身者被高已亲其进此话常与活正感见明问力理尔点文几定本公特做外孩相西果走将月十实向声车全信重三机工物气每并别真打太新比才便夫再书部水像眼等体却加电主界门利海受听表德少克代员许稜先口由死安写性马光白或住难望教命花结乐色更拉东神记处让母父应直字场平报友关放至张认接告入笑内英军候民岁往何度山觉路带万男边风解叫任金快原吃妈变通师立象数四失满战远格士音轻目条呢病始达深完今提求清王化空业思切怎非找片罗钱紶吗语元喜曾离飞科言干流欢约各即指合反题必该论交终林请医晚制球决窢传画保读运及则房早院量苦火布品近坐产答星精视五连司巴奇管类未朋且婚台夜青北队久乎越观落尽形影红爸百令周吧识步希亚术留市半热送兴造谈容极随演收首根讲整式取照办强石古华諣拿计您装似足双妻尼转诉米称丽客南领节衣站黑刻统断福城故历惊脸选包紧争另建维绝树系伤示愿持千史谁准联妇纪基买志静阿诗独复痛消社算义竟确酒需单治卡幸兰念举仅钟怕共毛句息功官待究跟穿室易游程号居考突皮哪费倒价图具刚脑永歌响商礼细专黄块脚味灵改据般破引食仍存众注笔甚某沉血备习校默务土微娘须试怀料调广蜖苏显赛查密议底列富梦错座参八除跑亮假印设线温虽掉京初养香停际致阳纸李纳验助激够严证帝饭忘趣支春集丈木研班普导顿睡展跳获艺六波察群皇段急庭创区奥器谢弟店否害草排背止组州朝封睛板角况曲馆育忙质河续哥呼若推境遇雨标姐充围案伦护冷警贝著雪索剧啊船险烟依斗值帮汉慢佛肯闻唱沙局伯族低玩资屋击速顾泪洲团圣旁堂兵七露园牛哭旅街劳型烈姑陈莫鱼异抱宝权鲁简态级票怪寻杀律胜份汽右洋范床舞秘午登楼贵吸责例追较职属渐左录丝牙党继托赶章智冲叶胡吉卖坚喝肉遗救修松临藏担戏善卫药悲敢靠伊村戴词森耳差短祖云规窗散迷油旧适乡架恩投弹铁博雷府压超负勒杂醒洗采毫嘴毕九冰既状乱景席珍童顶派素脱农疑练野按犯拍征坏骨余承置臓彩灯巨琴免环姆暗换技翻束增忍餐洛塞缺忆判欧层付阵玛批岛项狗休懂武革良恶恋委拥娜妙探呀营退摇弄桌熟诺宣银势奖宫忽套康供优课鸟喊降夏困刘罪亡鞋健模败伴守挥鲜财孤枪禁恐伙杰迹妹藸遍盖副坦牌江顺秋萨菜划授归浪听凡预奶雄升碃编典袋莱含盛济蒙棋端腿招释介烧误乾坤"
    for x in range(取出的数量):
        文本 += random.choice(部分汉字)
    return 文本


def 文本_取随机姓氏(取常见姓氏=False) -> str:
    '常见姓氏为自己设置挑选的,仅做参考'
    百家姓 = """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫柯房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊于惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭历戎祖武符刘景詹束龙叶幸司韶郜黎蓟溥印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阳郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂濮牛寿通边扈燕冀浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逮盍益桓公"""
    常见百家姓 = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛范彭郎鲁韦昌马苗凤花方俞任袁柳史唐费薛雷贺罗毕于齐萧尹姚顾孟平黄宋庞项祝董梁杜阮刘万丁石洪白田夏'
    if 取常见姓氏 == False:
        return random.choice(百家姓)
    else:
        return random.choice(常见百家姓)


def 文本_取随机手机号() -> str:
    号码前缀 = ['130', '131', '132', '134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '153', '155',
            '156', '157', '158', '159', '170', '171', '180', '182', '183', '185', '186', '187', '188', '189']
    尾号 = ''
    for x in range(8):
        尾号 += str(random.randint(0, 9))
    return random.choice(号码前缀) + 尾号


def 文本_取随机邮箱() -> str:
    邮箱后缀 = ['@qq.com', '@sina.com', '@126.com', '@163.com', '@hotmail.com', '@139.com', '@189.com', '@sohu.com',
            '@21cn.com', '@189.com', '@tom.com', '@aol.com', '@263.com', '@aliyun.com', '@foxmail.com', '@yeah.net']
    字母 = 字符 = 混合 = ""
    数字 = str(random.randint(1, 9))
    for x in range(random.randint(5, 11)): 数字 += str(random.randint(0, 9))
    for x in range(random.randint(5, 11)): 字母 += random.choice('qwertyuiopasdfghjklzxcvbnm')
    for x in range(random.randint(6, 11)): 字符 += random.choice('0123456789abcdefghijklnmopqrstuvwxyz')
    for x in range(random.randint(1, 6)): 混合 += random.choice('qwertyuiopasdfghjklzxcvbnm')
    for x in range(random.randint(3, 10)): 混合 += str(random.randint(0, 9))
    字符 = 字符[1:] if 字符.startswith('0') else 字符
    return random.choice([混合, 混合, 混合, 字母, 数字, 字符]) + random.choice(邮箱后缀)


def 文本_删左边(欲处理文本: str, 删除长度: int) -> str:
    return 取文本右边(欲处理文本, 取文本长度(欲处理文本) - 删除长度)


def 文本_删右边(欲处理文本: str, 删除长度: int) -> str:
    return 取文本左边(欲处理文本, 取文本长度(欲处理文本) - 删除长度)


def 文本_删中间(欲处理文本: str, 起始位置: int, 删除长度: int) -> str:
    return 取文本左边(欲处理文本, 起始位置) + 文本_删左边(欲处理文本, 起始位置 + 删除长度)


def 文本_取出文本中汉字(欲处理文本: str) -> str:
    '返回文本中的所有汉字'
    result = re.findall(r"[\u4e00-\u9fa5]", 欲处理文本)
    return "".join(result)


def 文本_逐字分割(欲处理文本: str) -> str:
    arr = []
    for item in 欲处理文本:
        arr.append(item)
    return arr


def 文本_颠倒(欲处理文本: str) -> str:
    return 欲处理文本[::-1]


def 文本_是否为汉字(欲处理文本: str) -> bool:
    '全汉字返回True'
    zhmodel = re.compile(u'[^\u4e00-\u9fa5]')  # 检查中文
    match = zhmodel.search(欲处理文本)
    if match:
        return False
    else:
        return True


# type 0大小写字母 1大写字母 2小写字母
def 文本区分_只取字母(欲处理文本: str, type=0) -> str:
    '返回文本中的所有小写字母'
    if type == 0:
        strArr = re.findall(r'[a-zA-Z]+', 欲处理文本)
    elif type == 1:
        strArr = re.findall(r'[A-Z]+', 欲处理文本)
    elif type == 2:
        strArr = re.findall(r'[a-z]+', 欲处理文本)
    else:
        pass
    if strArr:
        return "".join(strArr)


def 文本区分_只取数字(欲处理文本: str) -> str:
    '返回文本中的所有数字'
    strArr = re.findall(r'\d+', 欲处理文本)
    if strArr:
        return "".join(strArr)


def 判断文本(文本: str, 关键字: list) -> bool:
    if type(关键字) == str:
        index = 寻找文本(文本, 关键字)
        if index != -1:
            return True
        return False

    for item in 关键字:
        index = 寻找文本(文本, item)
        if index != -1:
            return True
    return False


def 判断文本s(文本: str, 关键字: list) -> bool:
    for item in 关键字:
        index = 寻找文本(文本, item)
        if index != -1:
            return item
    return ""


def 文本_取手机号码(欲处理文本: str) -> str:
    '取文本中的手机号码,列表格式'
    result = re.findall(r"1[3,4,5,6,7,8,9]\d{9}", 欲处理文本)
    if result:
        return result


def 文本_取IP地址(欲处理文本: str) -> str:
    '取文本中的IP地址,列表格式'
    result = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", 欲处理文本)
    if result:
        return result


def 文本_取电话号码(欲处理文本: str) -> str:
    '取文本中的电话号码,列表格式'
    result = re.findall(r"\d{3,4}[\s,-]?\d{7,8}", 欲处理文本)
    if result:
        return result


def 文本_取QQ号码(欲处理文本: str) -> str:
    '取文本中的QQ号码,列表格式,最多取11位数QQ号'
    result = re.findall(r"[1-9][0-9]{4,10}", 欲处理文本)
    if result:
        return result


def 文本_取邮政编码(欲处理文本: str) -> str:
    '中国邮政编码为6位数字,列表格式'
    result = re.findall(r"[1-9]\d{5}(?!\d)", 欲处理文本)
    if result:
        return result


def 文本_取身份证号码(欲处理文本: str) -> str:
    '中国的身份证为15位或18位,列表格式'
    result = re.findall(r"[1-9][0-9,X]{14,17}", 欲处理文本)
    if result:
        return result


def 文本_取双字节字符(欲处理文本: str) -> str:
    '汉字 大写符号是双字节 数字 字母 小写符号是单字节字符'
    result = re.findall(r"[^\x00-\xff]", 欲处理文本)
    return "".join(result)


def 文本_取网址(欲处理文本: str) -> str:
    '取带：//的网址,列表格式'
    result = re.findall(r"[a-zA-z]+://[^\s]*", 欲处理文本)
    if result:
        return result


def 文本_取IP跟端口(欲处理文本: str) -> str:
    '取IP地址带端口号,如：127.0.0.1:8080'
    result = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}", 欲处理文本)
    if result:
        return result


def 文本_取邮箱号码(欲处理文本: str) -> str:
    '取邮箱号码,列表格式'
    result = re.findall(r"[a-z0-9\.\-+_]{1,30}@[a-z0-9\.\-+_]{1,30}\.[a-z]{1,10}", 欲处理文本)
    if result:
        return result


def 文本_大小写翻转(欲处理文本: str) -> str:
    return 欲处理文本.swapcase()


def 文本_是否为大写字母(欲处理文本: str) -> bool:
    return 欲处理文本.isupper()


def 文本_是否为小写字母(欲处理文本: str) -> bool:
    return 欲处理文本.islower()


def 文本_是否为字母(欲处理文本: str) -> bool:
    return 欲处理文本.isalpha()


def 文本_是否为数字字母(欲处理文本: str) -> bool:
    return 欲处理文本.isalnum()


def 文本_是否为数字(欲处理文本: str) -> bool:
    return 欲处理文本.isdigit()


def 文本_取出现次数(欲处理文本: str, 欲查询的文本, 开始的位置=0, 结束的位置=0) -> int:
    结束的位置 = len(欲处理文本) if 结束的位置 < 1 else 结束的位置
    return 欲处理文本.count(欲查询的文本, 开始的位置, 结束的位置)


def 文本_单词首字母大写(欲处理文本) -> str:
    return 欲处理文本.title()


def 文本_填充空格_居中(欲处理文本: str, 填充目标长度: int) -> str:
    '将文本用空格填充到指定长度使欲处理文本居中'
    return 欲处理文本.center(填充目标长度)


def 文本_填充空格_左对齐(欲处理文本: str, 填充目标长度: int) -> str:
    '将文本用空格填充到指定长度使欲处理文本左对齐'
    return 欲处理文本.ljust(填充目标长度)


def 文本_填充空格_右对齐(欲处理文本: str, 填充目标长度: int) -> str:
    '将文本用空格填充到指定长度使欲处理文本右对齐'
    return 欲处理文本.rjust(填充目标长度)


def 文本_自动补零(欲处理文本: str, 填充目标长度: int) -> str:
    '将文本用0填充到指定长度使欲处理文本右对齐,如：0001'
    return 欲处理文本.zfill(填充目标长度)


def 数组_转文本(数组: list, 分隔符: str = "\r\n") -> str:
    return 分隔符.join(数组)


def 文本_判断文本前缀(欲处理文本: str, 开头的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> bool:
    '如果字符串为指定的开头返回True，否则返回False'
    结束的位置 = len(欲处理文本) if 结束的位置 < 1 else 结束的位置
    return 欲处理文本.startswith(开头的文本, 开始的位置, 结束的位置)


def 文本_判断文本后缀(欲处理文本: str, 结尾的文本: str, 开始的位置: int = 0, 结束的位置: int = 0) -> str:
    '如果字符串为指定的后缀返回True，否则返回False'
    结束的位置 = len(欲处理文本) if 结束的位置 < 1 else 结束的位置
    return 欲处理文本.endswith(结尾的文本, 开始的位置, 结束的位置)


def 文本_TAB转空格(欲处理文本: str, 转换的数量: int = 8) -> str:
    '把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8'
    return 欲处理文本.expandtabs(tabsize=转换的数量)


def 文本_取随机IP() -> str:
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))


def 文本_取中间_批量(欲处理文本: str, 前面的文本: str, 后面的文本: str) -> str:
    index = 0
    list = []
    while True:
        index = 欲处理文本.find(前面的文本, index)
        if index != -1:
            lastIndex = 欲处理文本.find(后面的文本, index + len(前面的文本))
            if lastIndex != -1:
                index = index + len(前面的文本)
                str = 欲处理文本[index:lastIndex]
                if len(str) > 0:
                    list.append(str)
            else:
                break
        else:
            break
    return list


# 使用教程
# https://github.com/mozillazg/python-pinyin
def 文本_汉字转拼音(欲处理文本, 连接符='', 拼音风格=0, 遍历多音=False, 无拼音处理=0, 严格规范=False):
    from pypinyin import Style, pinyin  # 需要安装拼音库 pip install pypinyin
    '默认返回全拼,拼音风格:0是不带声调的全拼,1是带声调的全拼,2是取声母部分,3是取首字母,无拼音处理：0是保留原始字符,1是忽略该字符,2是 替换为去掉 \\u 的 unicode 编码字符串'
    风格 = [Style.NORMAL, Style.TONE, Style.INITIALS, Style.FIRST_LETTER]
    处理 = ['default', 'ignore', 'replace']
    rStyle = 风格[0 if 拼音风格 > 3 or 拼音风格 < 0 else 拼音风格]
    Errors = 处理[0 if 无拼音处理 > 2 or 无拼音处理 < 0 else 无拼音处理]

    拼音 = ''
    拼音列表 = pinyin(hans=欲处理文本, style=rStyle, heteronym=遍历多音, errors=Errors, strict=严格规范)
    for x in 拼音列表:
        for i in x:
            拼音 = 拼音 + 连接符 + i
    return 拼音

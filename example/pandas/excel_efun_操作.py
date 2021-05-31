from pyefun import *
from pyefun.excel import *


# https://xlwt.readthedocs.io/en/latest/index.html

#############################
def 读取excel():
    excel = 打开excel("test.xls")

    print('sheet名称:', excel.取sheet名称())
    print('sheet数量:', excel.取sheet数量())

    sheet = excel.取sheet从名称("test")
    # sheet = excel.取sheet从索引(0)

    print(u'sheet %s 有 %d 行' % (sheet.取名称(), sheet.取行数()))
    print(u'sheet %s 有 %d 列' % (sheet.取名称(), sheet.取列数()))
    print('第二行内容:', sheet.取行所有内容(1))
    print('第三列内容:', sheet.取列所有内容(2))
    print('第二行第三列的值为:', sheet.取内容(1, 2))
    print('第二行第三列值的类型为:', type(sheet.取内容(1, 2)))


#############################
def 写出excel():
    excel = 创建Excel工作簿()
    sheet = excel.添加sheet('test')

    字体 = 创建Excel字体()
    字体.粗体 = True  # 字体加粗

    对齐方式 = 创建Excel对齐方式()
    对齐方式.水平方向 = 对齐方式.水平_左对齐

    # 创建样式对象
    样式1 = 创建Excel样式()
    样式2 = 创建Excel样式()
    样式1.字体 = 字体
    样式2.对齐方式 = 对齐方式

    # write 方法参数1：行，参数2：列，参数3：内容
    sheet.置内容(0, 1, '姓名', 样式1)
    sheet.置内容(0, 2, '年龄', 样式1)
    sheet.置内容(1, 1, '张三')
    sheet.置内容(1, 2, 50, 样式2)
    sheet.置内容(2, 1, '李四')
    sheet.置内容(2, 2, 30, 样式2)
    sheet.置内容(3, 1, '王五')
    sheet.置内容(3, 2, 40, 样式2)
    sheet.置内容(4, 1, '赵六')
    sheet.置内容(4, 2, 60, 样式2)
    sheet.置内容(5, 0, '平均年龄', 样式1)

    # 保存
    excel.保存("test.xls")


#############################


#
def avg(list):
    sumv = 0
    for i in range(len(list)):
        sumv += list[i]
    return int(sumv / len(list))


# # formatting_info 为 True 表示保留原格式
# excel = eExcel读取()
# wb = excel.打开Excel(文件路径='test.xls', 格式化信息=True)
# # 复制
# wbc = excel.复制为写操作excel()
#
# sh = excel.取sheet从索引(0)
# age_list = sh.取列所有内容(2)
# age_list = age_list[1:len(age_list) - 1]
# avg_age = avg(age_list)
#
# sh = wbc.取sheet从索引(0)
# # 设置左对齐
# alm = eExcel对齐方式()
# alm.水平方向 = alm.水平_右对齐
# style = eExcel样式()
# style.alignment = alm
# sh.置内容(5, 2, avg_age, style)
# wbc.save('test.xls')


def 打开一个excel文件并且编辑():
    excel读取 = 打开excel("test.xls")
    excel = excel读取.复制为写操作excel()

    sh = excel读取.取sheet从索引(0)
    age_list = sh.取列所有内容(2)
    print(age_list)
    age_list = age_list[1:len(age_list) - 1]
    print(age_list)
    avg_age = avg(age_list)
    print(avg_age)

    sh = excel.取sheet从索引(0)
    # 设置左对齐
    style = 创建Excel样式(对齐方式=创建Excel对齐方式(水平方向=Excel对齐方式.水平_右对齐))
    sh.置内容(5, 2, avg_age, style)
    excel.save('test.xls')


#############################
def 导出一个列表():
    excel = 创建Excel空工作簿()
    sheet = excel.添加sheet("sheet")

    样式 = 创建Excel样式(
        字体=创建Excel字体(字体名称="微软雅黑", 大小=20),
        对齐方式=创建Excel对齐方式(水平方向=Excel对齐方式.水平_右对齐,
                         垂直方向=Excel对齐方式.垂直_底端对齐,
                         自动换行=False),
        边框=创建Excel边框(1, 1, 1, 1, 2, 2, 2, 2),
        背景颜色=创建Excel背景颜色(5),
    )

    sheet.置内容(0, 0, "姓名", 样式)
    sheet.置内容(0, 1, "年龄", 样式)

    sheet.置列宽(0, 40)
    sheet.置列宽(1, 40)
    sheet.置行高(0, 100)

    for i in range(10):
        sheet.置内容(i + 1, 0, 文本_取随机姓氏() + 文本_取随机汉字(2), 样式)
        sheet.置内容(i + 1, 1, 取随机数(1, 100), 样式)

        sheet.置行高(i + 1, 100)

    excel.保存("test2.xls")


from PIL import Image


def 读入一个列表():
    excel = 打开excel("test2.xls", 编辑=True, 保留样式=True)
    print(excel.取sheet名称())
    # sheet = excel.取sheet从名称("sheet")
    sheet = excel.取sheet从索引(0)

    for x in range(sheet.取行数()):
        for y in range(sheet.取列数()):
            print("x:%s y:%s 内容:%s" % (x, y, sheet.取内容(x, y)))

    样式 = 创建Excel样式(
        对齐方式=创建Excel对齐方式(水平方向=Excel对齐方式.水平_居中对齐,
                         垂直方向=Excel对齐方式.垂直_居中对齐,
                         自动换行=True),
    )

    for x in range(sheet.取行数()):
        data = sheet.取行所有内容(x)
        print(data)
        # sheet写.置内容(x, 0, "空白")
        sheet.置内容(x, 0, "空白")
        # img = Image.open(r"C:\python\pyefun\pyefun\example\wxefun\1.jpg")
        # img.save(r"C:\python\pyefun\pyefun\example\wxefun\1.bmp")

        sheet.置行高(x + 1, 800)
        sheet.置内容(x, 2, "",样式)

        # 感觉很垃圾这个库 操作图片
        sheet.置图片从文件(x, 2, r"C:\python\pyefun\pyefun\example\wxefun\1.bmp", x=0, y=int(x*250), scale_x=1, scale_y=1)

    excel.保存("test3.xls")


# 写出excel()
# 读取excel()
# 打开一个excel文件并且编辑()
# 导出一个列表()
读入一个列表()

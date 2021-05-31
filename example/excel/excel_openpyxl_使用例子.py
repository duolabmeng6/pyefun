from pyefun import *
from pyefun.excel.excel_openpyxl import *

def 创建空白的工作簿导入数据():
    excel = Excel()
    excel.创建空白工作簿()
    data = excel.取所有sheet名称()
    print(data)

    excel.置当前sheet名称("一班班级数据")
    excel.置内容(1, 1, "学生名称")
    excel.置内容(1, 2, "学号")
    excel.置内容(1, 3, "语文成绩")
    for x in range(1, 51):
        excel.置内容(x + 1, 1, 文本_取随机姓氏() + 文本_取随机汉字(2))
        excel.置内容(x + 1, 2, x)
        excel.置内容(x + 1, 3, 取随机数(60, 100))

    excel.创建Sheet("二班班级数据")
    # excel.置当前sheet("二班班级数据")
    print(excel.取所有sheet名称())

    excel.置内容(1, 1, "学生名称")
    excel.置内容(1, 2, "学号")
    excel.置内容(1, 3, "语文成绩")
    for x in range(1, 51):
        excel.置内容(x + 1, 1, 文本_取随机姓氏() + 文本_取随机汉字(2))
        excel.置内容(x + 1, 2, x)
        excel.置内容(x + 1, 3, 取随机数(60, 100))

    excel.保存("test.xlsx")


def 读取excel数据():
    excel = Excel()
    excel.打开Excel("test.xlsx")
    print(excel.取行数())
    print(excel.取列数())
    print(excel.取所有sheet名称())
    print(excel.取当前sheet名称())
    #
    # for x in range(excel.取行数()):
    #     print("%s %s %s" % (
    #         excel.取内容(x + 1, 1),
    #         excel.取内容(x + 1, 2),
    #         excel.取内容(x + 1, 3),
    #     ))
    #
    # excel.置当前sheet("二班班级数据")
    # print(excel.取当前sheet名称())
    # for x in range(excel.取行数()):
    #     print("%s %s %s" % (
    #         excel.取内容(x + 1, 1),
    #         excel.取内容(x + 1, 2),
    #         excel.取内容(x + 1, 3),
    #     ))

    excel.置当前sheet("二班班级数据")
    print(excel.取当前sheet名称())
    excel.置列宽("A", 50)
    excel.置列宽("b", 50)
    excel.置列宽("C", 50)
    excel.合并单元格("A1:C3")

    for x in range(1, excel.取行数()):
        print(x)
        excel.置行高(x, 200)

        # excel.置单元格背景颜色(x,1,"FF0000")
        excel.置单元格对齐方式(x, 1,
                       对齐方式=Alignment(horizontal="center", vertical="center", wrap_text=True)
                       )
        excel.置单元格字体风格(x, 1,
                       字体名称=u"微软雅黑",
                       字体大小=22,
                       加粗=False,
                       斜体=False,
                       删除线=False,
                       颜色="FF0000",
                       )

        excel.置单元格字体风格(x, 2,
                       字体名称=u"微软雅黑",
                       字体大小=22,
                       加粗=False,
                       斜体=False,
                       删除线=False,
                       颜色="FF0000",
                       )
        excel.置单元格字体风格(x, 3,
                       字体名称=u"微软雅黑",
                       字体大小=22,
                       加粗=False,
                       斜体=False,
                       删除线=False,
                       颜色="FF0000",
                       )

        excel.置单元格边框(x, 1,
                     left=Side(border_style="thin", color="000000"),
                     right=Side(border_style="thin", color="000000"),
                     top=Side(border_style="thin", color="000000"),
                     bottom=Side(border_style="thin", color="000000"),
                     )

        excel.置图片("d%s" % x, 200, 200, "../wxefun/1.jpg")
    excel.保存("test2.xlsx")

    # for x in range(1,excel.取行数()):
    #     print(excel.取某行的所有内容(x))
    #
    # for x in range(1,excel.取列数()):
    #     print(excel.取某列的所有内容(x))


创建空白的工作簿导入数据()
读取excel数据()

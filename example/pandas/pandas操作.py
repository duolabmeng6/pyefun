from excel_efun import *

excel = eExcel读取()
excel.打开Excel("test.xlsx")

print('sheet名称:', excel.取sheet名称())
print('sheet数量:', excel.取sheet数量())
# 根据 sheet 索引获取 sheet
sheet = excel.取sheet从名称("test")
# sh = excel.取sheet从索引(0)

print(u'sheet %s 有 %d 行' % (sheet.取名称(), sheet.取行数()))
print(u'sheet %s 有 %d 列' % (sheet.取名称(), sheet.取列数()))
print('第二行内容:', sheet.取行所有内容(1))
print('第三列内容:', sheet.取列所有内容(2))
print('第二行第三列的值为:', sheet.取内容(1, 2))
print('第二行第三列值的类型为:', type(sheet.取内容(1, 2)))

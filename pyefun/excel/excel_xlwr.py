"""

.. Hint::
    xlwt 和 wlrd 封装的excel操作

    可能需要

    pip install xlutils
    pip install xlwt
    pip install xlrd


.. literalinclude:: ../../../example/excel_xlwr.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import xlwt
import xlrd
from xlutils.copy import copy


class Excel():
    def __init__(self):
        """
        __init__ 的功能说明（请补充）。

        """
        pass

    def 打开Excel(self, 文件路径, 编辑=False, 保留样式=False):
        """
        打开Excel 的功能说明（请补充）。

        Args:
            文件路径: 参数说明。
            编辑 (可选): 参数说明。默认值为 False。
            保留样式 (可选): 参数说明。默认值为 False。

        """
        pass
        self.工作簿读操作 = xlrd.open_workbook(filename=文件路径,
                                         # logfile=sys.stdout,
                                         verbosity=0,
                                         # use_mmap=USE_MMAP,
                                         file_contents=None,
                                         encoding_override=None,
                                         formatting_info=保留样式,
                                         on_demand=False,
                                         ragged_rows=False)

        self.sheetw = None
        self.编辑 = 编辑
        if self.编辑:
            self.工作簿写操作 = self.复制为写操作excel()

    def 复制为写操作excel(self):
        """
        复制为写操作excel 的功能说明（请补充）。

        """
        wb = copy(self.工作簿读操作)
        wb.wb = wb
        return Excel写工作簿(wb)

    def 取sheet从索引(self, 索引):
        """
        索引从0开始
        """
        sh = self.工作簿读操作.sheet_by_index(索引)

        if self.编辑:
            self.sheetw = self.工作簿写操作.wb.get_sheet(索引)
        return ExcelSheet(sh, sheetw=self.sheetw)

    def 取sheet从名称(self, 名称):
        """
        取sheet名称()
        """
        sh = self.工作簿读操作.sheet_by_name(名称)

        if self.编辑:
            self.sheetw = self.工作簿写操作.wb.get_sheet(名称)

        return ExcelSheet(sheet=sh, sheetw=self.sheetw)

    def 取sheet数量(self):
        """
        取sheet数量 的功能说明（请补充）。

        """
        return self.工作簿读操作.nsheets

    def 取sheet名称(self):
        """
        取sheet名称 的功能说明（请补充）。

        """
        return self.工作簿读操作.sheet_names()

    def 保存(self, 文件路径):
        """
        保存 的功能说明（请补充）。

        Args:
            文件路径: 参数说明。

        """
        pass
        self.工作簿写操作.保存(文件路径)


class ExcelSheet():
    def __init__(self, sheet: xlrd.sheet.Sheet = None, sheetw: xlwt.Worksheet = None):
        """
        __init__ 的功能说明（请补充）。

        Args:
            sheet (xlrd.sheet.Sheet, 可选): 参数说明。默认值为 None。
            sheetw (xlwt.Worksheet, 可选): 参数说明。默认值为 None。

        """
        pass
        self.sheet = sheet
        self.sheetw = sheetw

    def 取对象(self):
        """
        取对象 的功能说明（请补充）。

        """
        return self.sheet

    def 取行数(self):
        """
        取行数 的功能说明（请补充）。

        """
        return self.sheet.nrows

    def 取列数(self):
        """
        取列数 的功能说明（请补充）。

        """
        return self.sheet.ncols

    def 取名称(self):
        """
        取名称 的功能说明（请补充）。

        """
        return self.sheet.name

    def 取行所有内容(self, 行):
        """
        取行所有内容 的功能说明（请补充）。

        Args:
            行: 参数说明。

        """
        return self.sheet.row_values(行)

    def 取列所有内容(self, 列):
        """
        取列所有内容 的功能说明（请补充）。

        Args:
            列: 参数说明。

        """
        return self.sheet.col_values(列)

    def 取内容(self, 行, 列):
        """
        取内容 的功能说明（请补充）。

        Args:
            行: 参数说明。
            列: 参数说明。

        """
        return self.sheet.cell_value(行, 列)

    ### 要写出的库支持
    def 置内容(self, 行, 列, 内容, 样式=xlwt.Style.default_style):
        """
        置内容 的功能说明（请补充）。

        Args:
            行: 参数说明。
            列: 参数说明。
            内容: 参数说明。
            样式 (可选): 参数说明。默认值为 xlwt.Style.default_style。

        """
        self.sheetw.write(行, 列, 内容, 样式)

    def 置列宽(self, 列, 宽度):
        """
        置列宽 的功能说明（请补充）。

        Args:
            列: 参数说明。
            宽度: 参数说明。

        """
        self.sheetw.col(列).width = 宽度 * 256

    def 置行高(self, 行, 高度):
        """
        置行高 的功能说明（请补充）。

        Args:
            行: 参数说明。
            高度: 参数说明。

        """
        self.sheetw.row(行).height_mismatch = True
        self.sheetw.row(行).height = 高度 * 20

    def 置图片从文件(self, row, col, filename, x=0, y=0, scale_x=1, scale_y=1):
        """
        置图片从文件 的功能说明（请补充）。

        Args:
            row: 参数说明。
            col: 参数说明。
            filename: 参数说明。
            x (可选): 参数说明。默认值为 0。
            y (可选): 参数说明。默认值为 0。
            scale_x (可选): 参数说明。默认值为 1。
            scale_y (可选): 参数说明。默认值为 1。

        """
        self.sheetw.insert_bitmap(row=row,
                                  col=col,
                                  filename=filename,
                                  x=x,
                                  y=y,
                                  scale_x=scale_x,
                                  scale_y=scale_y)

    def 置图片从数据(self, row, col, data, x=0, y=0, scale_x=1, scale_y=1):
        """
        置图片从数据 的功能说明（请补充）。

        Args:
            row: 参数说明。
            col: 参数说明。
            data: 参数说明。
            x (可选): 参数说明。默认值为 0。
            y (可选): 参数说明。默认值为 0。
            scale_x (可选): 参数说明。默认值为 1。
            scale_y (可选): 参数说明。默认值为 1。

        """
        self.sheetw.insert_bitmap_data(row=row,
                                       col=col,
                                       data=data,
                                       x=x,
                                       y=y,
                                       scale_x=scale_x,
                                       scale_y=scale_y)


class Excel写工作簿():
    def __init__(self, wb: xlwt.Workbook = xlwt.Workbook()):
        """
        __init__ 的功能说明（请补充）。

        Args:
            wb (xlwt.Workbook, 可选): 参数说明。默认值为 xlwt.Workbook()。

        """
        self.wb = wb

    def 添加sheet(self, 名称):
        """
        添加sheet 的功能说明（请补充）。

        Args:
            名称: 参数说明。

        """
        pass
        sh = self.wb.add_sheet(名称)
        return ExcelSheet(sheetw=sh)

    def 取sheet从名称(self, 名称):
        """
        取sheet从名称 的功能说明（请补充）。

        Args:
            名称: 参数说明。

        """
        pass
        sh = self.wb.get_sheet(名称)
        return ExcelSheet(sheetw=sh)

    def 取sheet从索引(self, 索引):
        """
        取sheet从索引 的功能说明（请补充）。

        Args:
            索引: 参数说明。

        """
        pass
        sh = self.wb.get_sheet(索引)
        return ExcelSheet(sheetw=sh)

    def 保存(self, 文件路径):
        """
        保存 的功能说明（请补充）。

        Args:
            文件路径: 参数说明。

        """
        pass
        self.wb.save(文件路径)


class Excel字体(xlwt.Font):
    # self.height = 0x00C8  # 200: this is font with height 10 points
    # self.italic = False
    # self.struck_out = False
    # self.outline = False
    # self.shadow = False
    # self.colour_index = 0x7FFF
    # self.bold = False
    # self._weight = 0x0190  # 0x02BC gives bold font
    # self.escapement = self.ESCAPEMENT_NONE
    # self.underline = self.UNDERLINE_NONE
    # self.family = self.FAMILY_NONE
    # self.charset = self.CHARSET_SYS_DEFAULT
    # self.name = 'Arial'

    @property
    def 轮廓(self):
        """
        轮廓 的功能说明（请补充）。

        """
        return self.outline

    @轮廓.setter
    def 轮廓(self, value):
        """
        轮廓 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.outline = value

    @property
    def 阴影(self):
        """
        阴影 的功能说明（请补充）。

        """
        return self.shadow

    @阴影.setter
    def 阴影(self, value):
        """
        阴影 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.shadow = value

    @property
    def 字体名称(self):
        """
        字体名称 的功能说明（请补充）。

        """
        return self.name

    @字体名称.setter
    def 字体名称(self, value):
        """
        字体名称 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.name = value

    @property
    def 颜色(self):
        """
        颜色 的功能说明（请补充）。

        """
        return self.colour_index

    @颜色.setter
    def 颜色(self, value):
        """
        颜色 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.colour_index = value

    @property
    def 大小(self):
        """
        大小 的功能说明（请补充）。

        """
        return self.height

    @大小.setter
    def 大小(self, value):
        """
        大小 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.height = 20 * value

    @property
    def 下划线(self):
        """
        下划线 的功能说明（请补充）。

        """
        return self.underline

    @下划线.setter
    def 下划线(self, value):
        """
        下划线 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.underline = value

    @property
    def 斜体(self):
        """
        斜体 的功能说明（请补充）。

        """
        return self.italic

    @斜体.setter
    def 斜体(self, value):
        """
        斜体 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.italic = value

    @property
    def 粗体(self):
        """
        粗体 的功能说明（请补充）。

        """
        return self.bold

    @粗体.setter
    def 粗体(self, value):
        """
        粗体 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.bold = value

    @property
    def 删除线(self):
        """
        删除线 的功能说明（请补充）。

        """
        return self.struck_out

    @删除线.setter
    def 删除线(self, value):
        """
        删除线 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.struck_out = value


class Excel对齐方式(xlwt.Alignment):
    # HORZ_GENERAL                = 0x00
    水平_常规 = 0x00
    # HORZ_LEFT                   = 0x01
    水平_左对齐 = 0x01
    # HORZ_CENTER                 = 0x02
    水平_居中对齐 = 0x02
    # HORZ_RIGHT                  = 0x03
    水平_右对齐 = 0x03
    # HORZ_FILLED                 = 0x04
    水平_填满 = 0x04
    # HORZ_JUSTIFIED              = 0x05 # BIFF4-BIFF8X
    水平_两端对齐 = 0x05  # BIFF4-BIFF8X
    # HORZ_CENTER_ACROSS_SEL      = 0x06 # Centred across selection (BIFF4-BIFF8X)
    水平_中心选择 = 0x06  # Centred across selection (BIFF4-BIFF8X)
    # HORZ_DISTRIBUTED            = 0x07 # Distributed (BIFF8X)
    水平_分散 = 0x07  # Distributed (BIFF8X)

    # VERT_TOP                    = 0x00
    垂直_顶端对齐 = 0x00
    # VERT_CENTER                 = 0x01
    垂直_居中对齐 = 0x01
    # VERT_BOTTOM                 = 0x02
    垂直_底端对齐 = 0x02
    # VERT_JUSTIFIED              = 0x03 # Justified (BIFF5-BIFF8X)
    垂直_两端对齐 = 0x03  # Justified (BIFF5-BIFF8X)
    # VERT_DISTRIBUTED            = 0x04 # Distributed (BIFF8X)
    垂直_分散 = 0x04  # Distributed (BIFF8X)

    @property
    def 水平方向(self):
        """
        水平方向 的功能说明（请补充）。

        """
        return self.horz

    @水平方向.setter
    def 水平方向(self, value):
        """
        水平方向 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.horz = value

    @property
    def 垂直方向(self):
        """
        垂直方向 的功能说明（请补充）。

        """
        return self.vert

    @垂直方向.setter
    def 垂直方向(self, value):
        """
        垂直方向 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.vert = value

    @property
    def 自动换行(self):
        """
        自动换行 的功能说明（请补充）。

        """
        return self.wrap

    @自动换行.setter
    def 自动换行(self, value):
        """
        自动换行 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        if value:
            self.wrap = 1
        else:
            self.wrap = 0


class Excel样式(xlwt.XFStyle):
    pass

    @property
    def 字体(self):
        """
        字体 的功能说明（请补充）。

        """
        return self.font

    @字体.setter
    def 字体(self, value):
        """
        字体 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.font = value

    pass

    @property
    def 对齐方式(self):
        """
        对齐方式 的功能说明（请补充）。

        """
        return self.alignment

    @对齐方式.setter
    def 对齐方式(self, value):
        """
        对齐方式 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.alignment = value

    @property
    def 边框(self):
        """
        边框 的功能说明（请补充）。

        """
        return self.borders

    @边框.setter
    def 边框(self, value):
        """
        边框 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.borders = value

    @property
    def 背景颜色(self):
        """
        背景颜色 的功能说明（请补充）。

        """
        return self.pattern

    @背景颜色.setter
    def 背景颜色(self, value):
        """
        背景颜色 的功能说明（请补充）。

        Args:
            value: 参数说明。

        """
        self.pattern = value


def 打开Excel(文件路径, 编辑=False, 保留样式=False):
    """ 打开一个xls文件"""
    excel = Excel()
    excel.打开Excel(文件路径, 编辑=编辑, 保留样式=保留样式)

    return excel


def 创建Excel空工作簿():
    """ 创建一个空白的工作簿"""
    excel = Excel写工作簿()
    return excel


def 创建Excel字体(
        字体名称="宋体",
        轮廓=False,
        阴影=False,
        颜色=0,
        大小=12,
        下划线=False,
        斜体=False,
        粗体=False,
        删除线=False,
):
    """
    创建Excel字体 的功能说明（请补充）。

    Args:
        字体名称 (可选): 参数说明。默认值为 "宋体"。
        轮廓 (可选): 参数说明。默认值为 False。
        阴影 (可选): 参数说明。默认值为 False。
        颜色 (可选): 参数说明。默认值为 0。
        大小 (可选): 参数说明。默认值为 12。
        下划线 (可选): 参数说明。默认值为 False。
        斜体 (可选): 参数说明。默认值为 False。
        粗体 (可选): 参数说明。默认值为 False。
        删除线 (可选): 参数说明。默认值为 False。

    """
    字体 = Excel字体()
    字体.轮廓 = 轮廓
    字体.阴影 = 阴影
    字体.字体名称 = 字体名称
    字体.颜色 = 颜色
    字体.大小 = 大小
    字体.下划线 = 下划线
    字体.斜体 = 斜体
    字体.粗体 = 粗体
    字体.删除线 = 删除线
    return 字体


def 创建Excel对齐方式(
        水平方向=Excel对齐方式.水平_居中对齐,
        垂直方向=Excel对齐方式.垂直_居中对齐,
        自动换行=False
):
    """
    创建Excel对齐方式 的功能说明（请补充）。

    Args:
        水平方向 (可选): 参数说明。默认值为 Excel对齐方式.水平_居中对齐。
        垂直方向 (可选): 参数说明。默认值为 Excel对齐方式.垂直_居中对齐。
        自动换行 (可选): 参数说明。默认值为 False。

    """
    对齐方式 = Excel对齐方式()
    对齐方式.水平方向 = 水平方向
    对齐方式.垂直方向 = 垂直方向
    对齐方式.自动换行 = 自动换行
    return 对齐方式


def 创建Excel边框(左边边框=0,
              右边边框=0,
              顶边边框=0,
              底边边框=0,
              左边颜色=0x40,
              右边颜色=0x40,
              顶边颜色=0x40,
              底边颜色=0x40,
              ):
    """
    # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
    # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
    """
    borders = xlwt.Borders()
    borders.left = 左边边框
    borders.right = 右边边框
    borders.top = 顶边边框
    borders.bottom = 底边边框
    borders.left_colour = 左边颜色
    borders.right_colour = 右边颜色
    borders.top_colour = 顶边颜色
    borders.bottom_colour = 底边颜色
    return borders


def 创建Excel背景颜色(颜色索引=None):
    """
    0=黑色，1=白色，2=红色，3=绿色，4=蓝色，5=黄色，6=品红，7=青色，16=褐红色，17=深绿色，18=深蓝色，19=深黄色，几乎棕色），20=深品红，21=青色，22=浅灰色，23=深灰色
    """
    pattern = xlwt.Pattern()
    if 颜色索引 != None:
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 颜色索引

    return pattern


def 创建Excel保护(单元格锁定=1, 公式隐藏=0):
    """
    创建Excel保护 的功能说明（请补充）。

    Args:
        单元格锁定 (可选): 参数说明。默认值为 1。
        公式隐藏 (可选): 参数说明。默认值为 0。

    """
    protection = xlwt.Protection()
    protection.cell_locked = 单元格锁定
    protection.formula_hidden = 公式隐藏

    return protection


def 创建Excel样式(字体=创建Excel字体(), 对齐方式=创建Excel对齐方式(), 边框=创建Excel边框(), 背景颜色=创建Excel背景颜色(), 保护=创建Excel保护()):
    """
    创建Excel样式 的功能说明（请补充）。

    Args:
        字体 (可选): 参数说明。默认值为 创建Excel字体()。
        对齐方式 (可选): 参数说明。默认值为 创建Excel对齐方式()。
        边框 (可选): 参数说明。默认值为 创建Excel边框()。
        背景颜色 (可选): 参数说明。默认值为 创建Excel背景颜色()。
        保护 (可选): 参数说明。默认值为 创建Excel保护()。

    """
    样式 = Excel样式()
    样式.字体 = 字体
    样式.对齐方式 = 对齐方式
    样式.边框 = 边框
    样式.背景颜色 = 背景颜色
    样式.protection = 保护

    # self.num_format_str = 'General'
    # self.font = Formatting.Font()
    # self.alignment = Formatting.Alignment()
    # self.borders = Formatting.Borders()
    # self.pattern = Formatting.Pattern()
    # self.protection = Formatting.Protection()
    return 样式

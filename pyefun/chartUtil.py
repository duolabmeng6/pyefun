#-*- coding: utf-8 -*-
import random,io
import matplotlib.pyplot as plt
import numpy as np
from .public import *


图表颜色 = [
    '#F0F8FF', '#FAEBD7', '#00FFFF', '#7FFFD4', '#F0FFFF', '#F5F5DC', '#FFE4C4', '#FFEBCD', '#8A2BE2', '#A52A2A',
    '#DEB887', '#5F9EA0', '#7FFF00', '#D2691E', '#FF7F50', '#6495ED', '#FFF8DC', '#DC143C', '#00FFFF', '#008B8B',
    '#B8860B', '#A9A9A9', '#006400', '#BDB76B', '#8B008B', '#556B2F', '#FF8C00', '#9932CC', '#8B0000', '#E9967A',
    '#8FBC8F', '#483D8B', '#2F4F4F', '#00CED1', '#9400D3', '#FF1493', '#00BFFF', '#696969', '#1E90FF', '#B22222',
    '#FFFAF0', '#228B22', '#FF00FF', '#DCDCDC', '#F8F8FF', '#FFD700', '#DAA520', '#808080', '#008000', '#ADFF2F',
    '#F0FFF0', '#FF69B4', '#CD5C5C', '#4B0082', '#F0E68C', '#E6E6FA', '#FFF0F5', '#7CFC00', '#FFFACD', '#ADD8E6',
    '#F08080', '#E0FFFF', '#90EE90', '#D3D3D3', '#FFB6C1', '#FFA07A', '#20B2AA', '#87CEFA', '#778899', '#B0C4DE',
    '#00FF00', '#32CD32', '#FAF0E6', '#FF00FF', '#800000', '#66CDAA', '#BA55D3', '#9370DB', '#3CB371', '#7B68EE',
    '#00FA9A', '#48D1CC', '#C71585', '#191970', '#F5FFFA', '#FFE4E1', '#FFE4B5', '#FFDEAD', '#FDF5E6', '#808000',
    '#6B8E23', '#FFA500', '#FF4500', '#DA70D6', '#EEE8AA', '#98FB98', '#AFEEEE', '#DB7093', '#FFEFD5', '#FFDAB9',
    '#CD853F', '#FFC0CB', '#DDA0DD', '#B0E0E6', '#800080', '#FF0000', '#BC8F8F', '#4169E1', '#8B4513', '#FA8072',
    '#FAA460', '#2E8B57', '#FFF5EE', '#A0522D', '#C0C0C0', '#87CEEB', '#6A5ACD', '#708090', '#FFFAFA', '#00FF7F',
    '#4682B4', '#D2B48C', '#008080', '#D8BFD8', '#FF6347', '#40E0D0', '#EE82EE', '#F5DEB3', '#F5F5F5', '#FFFF00',
    '#9ACD32']


class 圆饼图:

    def __init__(self,标签列表=[],数值列表=[],颜色列表=[],间隔列表=[],起始角度=90,数值显示距离=0.6,保留小数位数=2,阴影=False,显示图例=True,宽高=()):
        self.plt = plt
        self.标签列表 = 标签列表
        self.数值列表 = 数值列表
        self.颜色列表 = 颜色列表
        self.间隔列表 = 间隔列表
        self.起始角度 = 起始角度 #逆时针起始角度设置
        self.数值显示位置 = 数值显示距离 #0-1,数值距圆心半径倍数距离
        self.保留小数位数 = 保留小数位数 #数值保留固定小数位
        self.显示阴影 = 阴影 #设置阴影
        self.宽高 = ()
        self.显示图例 = 显示图例

    @异常处理返回类型逻辑型
    def 生成(self,保存地址='',显示=True):
        '返回：图片二进制,标签列表,比例列表'
        fig = self.plt.figure()
        self.plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
        if self.宽高:
            self.plt.figure(figsize=(self.宽高[0],self.宽高[1]))

        if not self.标签列表 and not self.数值列表:
            self.标签列表 = ['张三','李四','王五']
            self.数值列表 = [111,222,333]

        数量 = len(self.标签列表)
        if not self.颜色列表 or len(self.颜色列表)<数量:
            颜色列表 = random.sample(图表颜色, 数量)
        else:
            颜色列表 = self.颜色列表

        if not self.间隔列表 or len(self.间隔列表)<数量:
            self.间隔列表 = [0 for i in range(数量)]

        patches, text1, text2 = self.plt.pie(self.数值列表,
                                             explode=self.间隔列表,
                                             labels=self.标签列表,
                                             colors=颜色列表,
                                             autopct='%.{}f%%'.format(self.保留小数位数),
                                             shadow=self.显示阴影,
                                             startangle=self.起始角度,
                                             pctdistance=self.数值显示位置)
        self.plt.axis('equal')

        if self.显示图例:
            self.plt.legend()

        if 保存地址:
            self.plt.savefig(保存地址)

        if 显示:
            self.plt.show()

        canvas=fig.canvas
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()

        标签列表=[]
        比例列表=[]
        for x in range(len(text1)):
            标签列表.append(text1[x].get_text())
            比例列表.append(text2[x].get_text())

        return data,标签列表,比例列表



class 柱状图:
    def __init__(self,宽高=(),标题="",横向标题="",纵向标题="",标签列表=[],数值列表=[],名称列表=[],颜色列表=[],柱宽=0.25,标题字体大小=20,显示项目名称=True):
        self.np = np
        self.plt = plt
        self.宽高 = 宽高
        self.标题 = 标题
        self.横向标题 = 横向标题
        self.纵向标题 = 纵向标题
        self.标签列表 = 标签列表
        self.数值列表 = [数值列表] if 数值列表 else []
        self.颜色列表 = 颜色列表
        self.名称列表 = 名称列表
        self.柱宽 = 柱宽
        self.显示项目名称 = 显示项目名称
        self.标题字体大小 = 标题字体大小

    @异常处理返回类型逻辑型
    def 加入新数值列表(self,数值列表):
        self.数值列表.append(数值列表)

    @异常处理返回类型逻辑型
    def 生成(self, 保存地址='', 显示=True):
        self.plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
        fig = self.plt.figure()
        if not self.标签列表 and not self.数值列表:
            self.标签列表 = ['a', 'b', 'c', 'd', 'e']
            self.数值列表 = [[33, 25, 15, 10, 3],[13, 15, 13, 5, 8]]

        数量 = len(self.标签列表)
        x = self.np.arange(数量)
        if self.宽高:
            self.plt.figure(figsize=(self.宽高[0], self.宽高[1]))

        if not self.名称列表 or len(self.名称列表)<len(self.数值列表):
            self.名称列表 = ['名称'+str(i) for i in range(数量)]

        if not self.颜色列表 or len(self.颜色列表) < 数量:
            颜色列表 = random.sample(图表颜色, 数量)
        else:
            颜色列表 = self.颜色列表

        for i in range(len(self.数值列表)):
            d = {'tick_label':self.标签列表} if i == 0 else {}
            if self.显示项目名称:
                d['label'] = self.名称列表[i]
            self.plt.bar(x+i*self.柱宽, self.数值列表[i], width=self.柱宽, color=颜色列表[i],**d)

            for a, b in zip(x, self.数值列表[i]):
                self.plt.text(a+i*self.柱宽, b + 0.1, b, ha='center', va='bottom')

        self.plt.xticks()
        if self.显示项目名称:
            self.plt.legend(loc="upper right")  # (左.left 右.right)防止label和图像重合显示不出来
        self.plt.ylabel(self.纵向标题)
        self.plt.xlabel(self.横向标题)
        self.plt.title(self.标题,fontdict = {'fontsize':self.标题字体大小})

        if 保存地址:
            self.plt.savefig(保存地址)

        if 显示:
            self.plt.show()
        canvas = fig.canvas
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()
        return data



class 横向柱状图:
    def __init__(self,宽高=(),标题="",横向标题="",纵向标题="",标签列表=[],数值列表=[],颜色值="",标题字体大小=20,显示项目名称=True):
        self.np = np
        self.plt = plt
        self.宽高 = 宽高
        self.标题 = 标题
        self.横向标题 = 横向标题
        self.纵向标题 = 纵向标题
        self.标签列表 = 标签列表
        self.数值列表 = 数值列表
        self.颜色 = 颜色值
        self.标题字体大小 = 标题字体大小

    @异常处理返回类型逻辑型
    def 生成(self, 保存地址='', 显示=True):
        self.plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
        fig = self.plt.figure()
        if self.宽高:
            self.plt.figure(figsize=(self.宽高[0], self.宽高[1]))

        if not self.颜色:
            self.颜色 = random.choice(图表颜色)

        if not self.标签列表 and not self.数值列表:
            self.标签列表 = ['a', 'b', 'c', 'd', 'e']
            self.数值列表 = [33, 25, 15, 10, 3]

        fig, ax = self.plt.subplots()
        ax.barh(self.标签列表, self.数值列表, color=self.颜色)
        labels = ax.get_xticklabels()
        self.plt.setp(labels, rotation=0, horizontalalignment='right')

        for a, b in zip(self.标签列表, self.数值列表):
            self.plt.text(b + 1, a, b, ha='center', va='center')

        self.plt.ylabel(self.纵向标题)
        self.plt.xlabel(self.横向标题)
        self.plt.title(self.标题,fontdict = {'fontsize':self.标题字体大小})

        if 保存地址:
            self.plt.savefig(保存地址)

        if 显示:
            self.plt.show()

        canvas = fig.canvas
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()
        return data


class 重叠柱状图:
    def __init__(self,宽高=(),标题="",横向标题="",纵向标题="",标签列表=[],数值列表=[],名称列表=[],颜色列表=[],柱宽=None,标题字体大小=20,显示项目名称=True):
        self.np = np
        self.plt = plt
        self.宽高 = 宽高
        self.标题 = 标题
        self.横向标题 = 横向标题
        self.纵向标题 = 纵向标题
        self.标签列表 = 标签列表
        self.数值列表 = [数值列表] if 数值列表 else []
        self.颜色列表 = 颜色列表
        self.名称列表 = 名称列表
        self.柱宽 = 柱宽
        self.显示项目名称 = 显示项目名称
        self.标题字体大小 = 标题字体大小

    @异常处理返回类型逻辑型
    def 加入新数值列表(self,数值列表):
        self.数值列表.append(数值列表)

    @异常处理返回类型逻辑型
    def 生成(self, 保存地址='', 显示=True):
        self.plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
        fig = self.plt.figure()
        if not self.标签列表 and not self.数值列表:
            self.标签列表 = ['a', 'b', 'c', 'd', 'e']
            self.数值列表 = [[33, 25, 15, 10, 9],[13, 15, 13, 5, 8]]

        数量 = len(self.标签列表)
        x = self.np.arange(数量)
        if self.宽高:
            self.plt.figure(figsize=(self.宽高[0], self.宽高[1]))

        if not self.名称列表 or len(self.名称列表)<len(self.数值列表):
            self.名称列表 = ['名称'+str(i) for i in range(数量)]

        if not self.颜色列表 or len(self.颜色列表) < 数量:
            颜色列表 = random.sample(图表颜色, 数量)
        else:
            颜色列表 = self.颜色列表

        for i in range(len(self.数值列表)):
            d = {'tick_label':self.标签列表} if i == 0 else {}
            if self.显示项目名称:
                d['label'] = self.名称列表[i]
            if self.柱宽:
                d['width'] = self.柱宽
            self.plt.bar(self.标签列表, self.数值列表[i], color=颜色列表[i],**d)
            for a, b in zip(x, self.数值列表[i]):
                self.plt.text(a, b + 0.1, b, ha='center', va='bottom')
        self.plt.xticks(self.np.arange(数量), self.标签列表, rotation=0, fontsize=10)

        if self.显示项目名称:
            self.plt.legend(loc="upper right")  # (左.left 右.right)防止label和图像重合显示不出来
        self.plt.ylabel(self.纵向标题)
        self.plt.xlabel(self.横向标题)
        self.plt.title(self.标题,fontdict = {'fontsize':self.标题字体大小})

        if 保存地址:
            self.plt.savefig(保存地址)

        if 显示:
            self.plt.show()

        canvas = fig.canvas
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()
        return data



class 折线图:
    def __init__(self,宽高=(),标题="",横向标题="",纵向标题="",标签列表=[],数值列表=[],名称列表=[],颜色列表=[],标题字体大小=20,显示项目名称=True,显示数值=True,显示圆点=True):
        self.np = np
        self.plt = plt
        self.宽高 = 宽高
        self.标题 = 标题
        self.横向标题 = 横向标题
        self.纵向标题 = 纵向标题
        self.标签列表 = 标签列表
        self.数值列表 = [数值列表] if 数值列表 else []
        self.颜色列表 = 颜色列表
        self.名称列表 = 名称列表
        self.显示项目名称 = 显示项目名称
        self.标题字体大小 = 标题字体大小
        self.显示数值 = 显示数值
        self.显示圆点 = 显示圆点

    @异常处理返回类型逻辑型
    def 加入新数值列表(self,数值列表):
        self.数值列表.append(数值列表)

    @异常处理返回类型逻辑型
    def 生成(self, 保存地址='', 显示=True):
        self.plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
        fig = self.plt.figure()
        if not self.标签列表 and not self.数值列表:
            self.标签列表 = ['a', 'b', 'c', 'd', 'e']
            self.数值列表 = [[33, 25, 15, 10, 3],[13, 15, 13, 5, 8]]

        数量 = len(self.标签列表)
        x = self.np.arange(数量)
        if self.宽高:
            self.plt.figure(figsize=(self.宽高[0], self.宽高[1]))

        if not self.名称列表 or len(self.名称列表)<len(self.数值列表):
            self.名称列表 = ['名称'+str(i) for i in range(数量)]

        if not self.颜色列表 or len(self.颜色列表) < 数量:
            颜色列表 = random.sample(图表颜色, 数量)
        else:
            颜色列表 = self.颜色列表

        for i in range(len(self.数值列表)):
            d = {}
            if self.显示项目名称:
                d['label'] = self.名称列表[i]
            if self.显示圆点:
                d['marker'] = '.'

            self.plt.plot(self.标签列表,self.数值列表[i],color=颜色列表[i],linewidth=1,mfc='w',markersize=10,mfcalt='b',**d)

            if self.显示数值:
                for a, b in zip(self.标签列表, self.数值列表[i]):
                    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)

        if self.显示项目名称:
            self.plt.legend(loc="upper right")  # (左.left 右.right)防止label和图像重合显示不出来
        self.plt.ylabel(self.纵向标题)
        self.plt.xlabel(self.横向标题)
        self.plt.title(self.标题,fontdict = {'fontsize':self.标题字体大小})

        #加虚线背景 透明度1 去掉是实线
        self.plt.grid(alpha=1,linestyle=':')

        if 保存地址:
            self.plt.savefig(保存地址)

        if 显示:
            self.plt.show()

        canvas = fig.canvas
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()
        return data
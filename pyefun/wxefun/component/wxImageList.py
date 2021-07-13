import wx

class 图片组类(wx.ImageList):
    def 加入图片(self, 文件路径, 宽度=0, 高度=0):
        img = wx.Image(文件路径, wx.BITMAP_TYPE_ANY)
        if 宽度 == 0:
            img = img.Scale(64, 64)
        else:
            img = img.Scale(宽度, 高度)

        img = img.ConvertToBitmap()
        return super().Add(img)

    def 加入(self, *__args):
        return super().Add(*__args)

    def 创建(self, width, height, mask=True, initialCount=1):
        return super().Create(width, height, mask, initialCount)

    def 绘制(self, index, dc, x, y, flags=None, solidBackground=False):
        return super().Draw(index, dc, x, y, flags, solidBackground)

    def 取位图(self, index):
        return super().GetBitmap(index)

    def 取Icon(self, index):
        return super().GetIcon(index)

    def 取图片数量(self):
        return super().GetImageCount(self)

    def 取大小(self, index=None):
        return super().GetSize(index)

    def 删除(self, index):
        return super().Remove(index)

    def 删除所有(self):
        return super().RemoveAll(self)

    def 替换(self, index, *__args):
        return super().Replace(index, *__args)

    def __init__(self, width=None, height=None, mask=True, initialCount=1):
        return super().__init__(width, height, mask, initialCount)

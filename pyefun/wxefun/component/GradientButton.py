from .wxControl import *
import wx.lib.agw.gradientbutton as gradientbutton

class 图文按钮L(gradientbutton.GradientButton, 公用方法):
    pass

    def 是否允许通过单击获取焦点(self):
        return self.AcceptsFocus()

    def 取最佳尺寸(self):
        '返回一个元组,(宽，高),覆盖基类虚拟。根据标签和边框尺寸确定按钮的最佳尺寸。'
        return self.DoGetBestSize()

    def 取渐变底纹底端颜色(self):
        return self.GetBottomEndColour()

    def 取渐变底纹顶端颜色(self):
        return self.GetTopEndColour()

    def 取渐变底纹底部起始颜色(self):
        return self.GetBottomStartColour()

    def 取渐变底纹按下底部起始颜色(self):
        return self.GetPressedBottomColour()

    def 取渐变底纹按下顶部起始颜色(self):
        return self.GetPressedTopColour()

    def 取渐变阴影顶部起始颜色(self):
        return self.GetTopStartColour()

    @组件_异常检测
    def 置各状态颜色(self,起始色,前景色):
        '设置底部，顶部，按下和前景色,起始色–用于底部，顶部和压制的基础颜色,前景色 –用于文本的颜色'
        return self.SetBaseColours(起始色,前景色)

    @组件_异常检测
    def 置图片(self,图片):
        return self.SetBitmapLabel(图片)

    @组件_异常检测
    def 置渐变底纹底端颜色(self,颜色):
        return self.SetBottomEndColour(颜色)

    @组件_异常检测
    def 置渐变底纹顶部底部颜色(self,颜色):
        return self.SetBottomStartColour(颜色)

    @组件_异常检测
    def 置默认按钮(self):
        return self.SetDefault()

    @组件_异常检测
    def 置最佳尺寸(self):
        '将按钮调整为最佳尺寸'
        self.SetInitialSize()

    @组件_异常检测
    def 置渐变阴影下底部开始颜色(self,颜色):
        return self.SetPressedBottomColour(颜色)

    @组件_异常检测
    def 置渐变阴影设置按下顶部起始颜色(self,颜色):
        return self.SetPressedTopColour(颜色)

    @组件_异常检测
    def 置渐变底纹顶端颜色(self,颜色):
        return self.SetTopEndColour(颜色)

    @组件_异常检测
    def 置渐变底纹顶部起始颜色(self,颜色):
        return self.SetTopStartColour(颜色)

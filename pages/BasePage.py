'''
所有界面的父类
'''
from locals import PAGETYPE,MODE
from pygame import font

class BasePage:
    # 当前页面类型
    pageType = PAGETYPE.SPLASH
    # 模式
    mode = MODE.SINGLE
    def __init__(self,window):
        '''
        :param window:需要展示的窗口
        '''
        self.window = window
        # 大字体
        self.bigFont = font.Font('resources/happy.ttf',100)
        # 中字体
        self.middleFont = font.Font('resources/happy.ttf',50)
        # 中小字体
        self.middleSmallFont = font.Font('resources/happy.ttf',30)
        # 小字体
        self.smallFont = font.Font('resources/happy.ttf',18)


    def display(self):
        '''
        展示当前界面
        :return:
        '''
        pass
    def keyDown(self,key):
        '''
        按下的事件
        :param key:按下的键
        :return:
        '''

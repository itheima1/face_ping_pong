from pygame.locals import KEYDOWN,QUIT
from sys import exit
from pages.BasePage import BasePage
from pygame import init,display,time,event,quit
from pages.SplashPage import SplashPage
from pages.GamePage import GamePage
from pages.GameOverPage import GameOverPage
from locals import WINDOW_WIDTH,WINDOW_HEIGHT,PAGETYPE
from cv2 import destroyAllWindows

def start():
    # 初始化
    init()
    # 创建窗口
    window = display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    # 设置标题
    display.set_caption('乒乓球')
    # Clock
    clock = time.Clock()
    # 初始界面
    page = SplashPage(window)
    # 渲染引擎
    while True:
        # 控制帧率
        clock.tick(40)
        # 选择不同的界面
        if BasePage.pageType==PAGETYPE.SPLASH and not isinstance(page,SplashPage):
            page = SplashPage(window)
        elif BasePage.pageType==PAGETYPE.GAME and not isinstance(page,GamePage):
            page = GamePage(window)
        elif BasePage.pageType==PAGETYPE.GAMEOVER and not isinstance(page,GameOverPage):
            page = GameOverPage(window)

        # 渲染界面
        page.display()
        # 刷新
        display.flip()
        if event.get(QUIT):
            # 退出pygame
            quit()
            # 清理所有的cv窗口
            destroyAllWindows()
            # 退出程序
            exit()
        # 获取按下的事件
        eventList = event.get(KEYDOWN)
        # 如果按下的事件不为空,传递到各个界面中
        if eventList:
            page.keyDown(eventList[0].key)
            # 获取一次事件
            event.get()
        # 清空事件
        event.get()

if __name__ == '__main__':
    start()
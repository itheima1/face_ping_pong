from pages.BasePage import BasePage
from locals import WHITE,WINDOW_WIDTH,WINDOW_HEIGHT,PAGETYPE

class GameOverPage(BasePage):
    def __init__(self,window):
        super(GameOverPage, self).__init__(window)
        # Game
        self.gameSurface = self.middleFont.render('Game', True, WHITE)
        # Over
        self.overSurface = self.middleFont.render('Over', True, WHITE)
        # 获取Game和Over的矩形
        self.gameRect = self.gameSurface.get_rect()
        self.overRect = self.overSurface.get_rect()
        # 设置底部中间位置
        self.gameRect.midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.overRect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        # 提示文本
        self.promotSurface = self.smallFont.render('Press a key to play', True, (255, 0, 0))
        # 获取矩形
        self.promotRect = self.promotSurface.get_rect()
        # 设置中心点
        self.promotRect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 20)

    def display(self):
        # 展示Game和Over
        self.window.blit(self.gameSurface, self.gameRect)
        self.window.blit(self.overSurface, self.overRect)
        # 显示提示
        self.window.blit(self.promotSurface, self.promotRect)

    def keyDown(self,key):
        # 按下任何按键,重新开始
        BasePage.pageType = PAGETYPE.SPLASH
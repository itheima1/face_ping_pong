from pages.BasePage import BasePage
from pygame import transform,image
from locals import MODE,GREEN,WINDOW_WIDTH,WINDOW_HEIGHT,WHITE,BLACK,PAGETYPE
from pygame.locals import K_UP,K_DOWN,K_RETURN


class SplashPage(BasePage):
    def __init__(self, window):
        super(SplashPage, self).__init__(window)
        #------------------------- 当前选中模式 -------------------------#
        # 模式1：单人模式
        # 模式2：双人模式
        self.mode = MODE.SINGLE
        # ------------------------- 标题 -------------------------#
        # 标题文本
        self.snakeSurface = self.middleFont.render('Ping Pang', True, GREEN)
        # 获取文本的矩形
        self.snakeRect = self.snakeSurface.get_rect()
        # 设置矩形中心点
        self.snakeRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 200)
        # ------------------------- 球拍图片 -------------------------#
        # 乒乓球拍
        racketSurface = image.load('image/pai.png')
        # 球拍的宽度和高度
        w = racketSurface.get_width()
        h = racketSurface.get_height()
        self.racketSurface = transform.scale(racketSurface, (w // 12, h // 12))
        # 球拍举行
        self.racketRect = self.racketSurface.get_rect()
        # 设置矩形中心点
        self.racketRect.center = (WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 2 - 40)
        # ------------------------- 单人模式文本 -------------------------#
        self.singleSurface = self.middleSmallFont.render('单人模式', True, WHITE)
        # 获取文本的矩形
        self.singleRect = self.singleSurface.get_rect()
        # 设置矩形中心点
        self.singleRect.center = (WINDOW_WIDTH / 2 + 50, WINDOW_HEIGHT / 2 - 50)
        # ------------------------- 双人模式文本 -------------------------#
        self.doubleSurface = self.middleSmallFont.render('双人模式', True, WHITE)
        # 获取文本的矩形
        self.doubleRect = self.doubleSurface.get_rect()
        # 设置矩形中心点
        self.doubleRect.center = (WINDOW_WIDTH / 2 + 50, WINDOW_HEIGHT / 2 + 50)
        # ------------------------- 提示文本 -------------------------#
        # 提示文本
        self.promotSurface = self.smallFont.render('select a mode to play', True, (255, 0, 0))
        # 获取矩形
        self.promotRect = self.promotSurface.get_rect()
        # 设置中心点
        self.promotRect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 20)

    def display(self):
        # 填充背景
        self.window.fill(BLACK)
        # 显示标题
        self.window.blit(self.snakeSurface, self.snakeRect)
        # 单人模式
        self.window.blit(self.singleSurface, self.singleRect)
        # 双人模式
        self.window.blit(self.doubleSurface, self.doubleRect)
        # 球拍
        self.window.blit(self.racketSurface, self.racketRect)
        # 显示提示
        self.window.blit(self.promotSurface, self.promotRect)

    def switchMode(self,direction):
        '''
        切换模式展示
        :param direction: 向上 1或 向下2
        :return:
        '''
        if direction==1 and self.mode!=MODE.SINGLE:
            # 设置矩形中心点
            self.racketRect.center = (WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 2 - 40)
            self.mode = MODE.SINGLE
        elif direction==2 and self.mode!=MODE.DOUBLE:
            # 设置矩形中心点
            self.racketRect.center = (WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 2 + 40)
            self.mode = MODE.DOUBLE
        # 刷新界面
        self.display()


    def keyDown(self, key):
        # 上下切换游戏模式
        if key==K_UP:
            self.switchMode(1)
        elif key==K_DOWN:
            self.switchMode(2)
        elif key==K_RETURN:
            # 修改游戏模式
            BasePage.mode = self.mode
            BasePage.pageType = PAGETYPE.GAME



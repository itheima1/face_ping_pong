from pages.BasePage import BasePage
from pygame.locals import K_SPACE,K_TAB
from locals import PATH_TO_CKPT,MODE,PAGETYPE,WHITE,WINDOW_WIDTH,WINDOW_HEIGHT
from numpy import squeeze,rot90
from cv2 import VideoCapture,cvtColor,COLOR_BGR2RGB
from utils.TensoflowFaceDector import TensoflowFaceDector
from pygame import image,surfarray,Rect,display,transform


class GamePage(BasePage):
    def __init__(self, window):
        super(GamePage, self).__init__(window)
        # ------------------------- 游戏是否结束 -------------------------#
        self.hasGameOver = False
        # ------------------------- 左右分数 -------------------------#
        self.leftScore = 0
        self.rightScore = 0
        # ------------------------- 游戏模式 -------------------------#
        # 检测人脸的个数
        if BasePage.mode == MODE.SINGLE:
            self.faceCount = 1
        elif BasePage.mode == MODE.DOUBLE:
            self.faceCount = 2
        # ------------------------- 暂停 -------------------------#
        # 是否暂停
        self.isPause = False
        # 暂停文字
        # 标题文本
        self.pauseSurface = self.middleFont.render('Pause', True, WHITE)
        # 获取文本的矩形
        self.pauseRect = self.pauseSurface.get_rect()
        # 设置矩形中心点
        self.pauseRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        # ------------------------- 检测的人脸方框数据 -------------------------#
        self.faceRects = []
        # ------------------------- 存放球拍数据 -------------------------#
        self.racketSurfaces = []
        # ------------------------- 球拍 -------------------------#
        # 乒乓球拍
        self.racketSurface = image.load('image/pai.png')
        # 球拍的宽度和高度
        self.racketW = self.racketSurface.get_width()
        self.racketH = self.racketSurface.get_height()

        # ------------------------- 小球位置 -------------------------#
        # 小球位置
        self.pos_x = 300  # 矩形的X轴坐标
        self.pos_y = 250  # 矩形的Y轴坐标
        # 小球x和y轴分速度
        self.vel_x = 24  # X轴分速度
        self.vel_y = 12  # Y轴分速度
        # ------------------------- 球 -------------------------#
        # 乒乓球拍
        ballSurface = image.load('image/ball.png')
        # 球拍的宽度和高度
        w = ballSurface.get_width()
        h = ballSurface.get_height()
        self.ballSurface = transform.scale(ballSurface, (w // 20, h // 20))
        # 球矩形
        self.ballRect = self.ballSurface.get_rect()
        # 球的宽度和高度
        self.ballW = self.ballRect.width
        self.ballH = self.ballRect.height

        # 设置矩形中心点
        self.ballRect.topleft = (self.pos_x, self.pos_y)

        # tensorflow检测类
        self.tfDetector = TensoflowFaceDector(PATH_TO_CKPT)
        # ---------------------- 读取配置获取摄像头id ---------------------- #
        f = open('config/config.txt')
        lines = f.readlines()
        for line in lines:
            if line.startswith('camera_index'):
                CAMERA_INDEX = int(line[line.index(':')+1:])
            elif line.startswith('game_over_score'):
                self.game_over_score = int(line[line.index(':')+1:])
        print('---------------摄像头id:',CAMERA_INDEX)
        # 摄像头
        self.camera = VideoCapture(CAMERA_INDEX)
        self.camera.set(3, WINDOW_WIDTH)
        self.camera.set(4, WINDOW_HEIGHT)

    def getCamFrame(self):
        '''
        摄像头获取一帧数据
        :param camera: 摄像头
        :return:
        '''
        # 清空人脸方框数据
        self.faceRects.clear()
        if not self.camera.isOpened():
            print('摄像头没有打开')
            return None
        # 获取图像
        retval, frame = self.camera.read()

        if retval:
            print('成功-------------------------------------------------------')
            frame = cvtColor(frame, COLOR_BGR2RGB)
            [h, w] = frame.shape[:2]
            # tensorflow检测人脸
            (boxes, scores, classes, num_detections) = self.tfDetector.run(frame)

            boxes = squeeze(boxes)
            scores = squeeze(scores)
            for i in range(0, self.faceCount):
                if scores[i] > 0.3:
                    ymin, xmax, ymax, xmin = boxes[i, 0], boxes[i, 1], boxes[i, 2], boxes[i, 3]
                    left, right, top, bottom = (xmin * w, xmax * w, ymin * h, ymax * h)
                    # 处理左右坐标
                    left = WINDOW_WIDTH - left
                    right = WINDOW_WIDTH - right
                    self.faceRects.append((left, right, top, bottom))
                    print('--------left', left, ' right', right)
                    # cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 255), 2)

            frame = rot90(frame)
            frame = surfarray.make_surface(frame)
            return frame
        else:
            print('失败-------------------------------------------------------')
        return None

    def handleSingleModeCollision(self):
        '''单人模式碰撞'''
        for _, rackRect in self.racketSurfaces:
            left = rackRect[0]
            top = rackRect[1]
            width = rackRect[2]
            height = rackRect[3]

            # 右侧矩形
            rightRect = Rect(left + width - 1, top, 1, height * 2 // 3)
            # 小球从右侧过来 是否和右侧碰撞
            if rightRect.colliderect(self.ballRect) and self.vel_x < 0:
                self.vel_x = abs(self.vel_x)
                self.rightScore+=1
                return

            # 左侧矩形
            leftRect = Rect(left, top, 1, height * 2 // 3)
            # 从左侧过来  是否和左侧碰撞
            if leftRect.colliderect(self.ballRect)and self.vel_x > 0:
                self.vel_x = -abs(self.vel_x)
                self.leftScore+=1
                return


    def handleDoubleModeCollision(self):
        '''双人模式碰撞'''
        for _, rackRect in self.racketSurfaces:
            left = rackRect[0]
            top = rackRect[1]
            width = rackRect[2]
            height = rackRect[3]
            # 中间的x
            centerX = left + width / 2
            # 判断左右位置
            if centerX < WINDOW_WIDTH / 2:
                # print('左侧--------------------------------------------------------------------','left',left,' right',right)
                # 左侧
                # 右侧矩形
                rightRect = Rect(left + width - 1, top, 1, height * 2 // 3)
                # 小球从右侧过来 是否和右侧碰撞
                if rightRect.colliderect(self.ballRect) and self.vel_x < 0:
                    self.vel_x = abs(self.vel_x)
                    return
            else:
                # print('右侧--------------------------------------------------------------------')
                # 右侧
                # 左侧矩形
                leftRect = Rect(left, top, 1, height * 2 // 3)
                # 从左侧过来  是否和左侧碰撞
                if leftRect.colliderect(self.ballRect) and self.vel_x > 0:
                    self.vel_x = -abs(self.vel_x)
                    return

    def handleCollision(self):
        '''处理球拍和小球碰撞'''
        if self.mode == MODE.SINGLE:
            self.handleSingleModeCollision()
        elif self.mode == MODE.DOUBLE:
            self.handleDoubleModeCollision()

    def display(self):
        # 是否暂停
        if self.isPause:
            self.window.blit(self.pauseSurface, self.pauseRect)
            return
        # 获取一帧画面
        frame = self.getCamFrame()
        # 如果没有画面不做处理
        if not frame:
            print('没有获取画面')
            return
        # 展示画面
        self.window.blit(frame, (0, 0))
        # 展示人脸球拍数据
        self.showRacket()
        # 处理球拍和小球碰撞
        self.handleCollision()
        # 展示乒乓球
        self.showBall()
        # 显示分数
        self.showScore()
        if not self.hasGameOver and self.mode==MODE.DOUBLE:
            # 游戏结束判断
            self.gameOver()

    def gameOver(self):
        '''游戏结束判断'''
        if self.leftScore >= self.game_over_score or self.rightScore >= self.game_over_score:
            # 游戏结束标示
            self.hasGameOver = True
            # 再展示一次
            self.display()
            # 刷新
            display.flip()
            # 修改页面标示
            BasePage.pageType = PAGETYPE.GAMEOVER

    def showSingleModeScore(self):
        '''单人模式分数'''
        # 标题文本
        self.leftScoreSurface = self.middleFont.render('左击:{}'.format(self.leftScore), True, WHITE)
        self.rightScoreSurface = self.middleFont.render('右击:{}'.format(self.rightScore), True, WHITE)
        # 显示分数
        self.window.blit(self.leftScoreSurface, (100, 50))
        self.window.blit(self.rightScoreSurface, (WINDOW_WIDTH - 200, 50))

    def showDoubleModeScore(self):
        '''双人模式分数'''
        # 标题文本
        self.leftScoreSurface = self.middleFont.render('{}'.format(self.leftScore), True, WHITE)
        self.rightScoreSurface = self.middleFont.render('{}'.format(self.rightScore), True, WHITE)
        # 显示分数
        self.window.blit(self.leftScoreSurface, (100,50))
        self.window.blit(self.rightScoreSurface, (WINDOW_WIDTH-100,50))

    def showScore(self):
        '''显示分数'''
        # 单人模式不显示分数
        if self.mode == MODE.SINGLE:
            self.showSingleModeScore()
        if self.mode == MODE.DOUBLE:
            self.showDoubleModeScore()

    def constructRacketDatas(self):
        '''根据人脸方框构建球拍数据'''
        # 清空数据
        self.racketSurfaces.clear()
        for face in self.faceRects:
            left = face[0]
            right = face[1]
            top = face[2]
            bottom = face[3]

            w = right - left
            h = bottom - top
            # 中心点
            centerP = left + w // 2, top + h // 2
            # 左侧赢  右侧不用展示球拍 右侧赢  左侧不需要展示
            if (self.leftScore >= 5 and centerP[0] > WINDOW_WIDTH / 2) or (
                    self.rightScore >= 5 and centerP[0] < WINDOW_WIDTH / 2):
                continue
            # 缩小系数
            if w > h:
                # 缩小倍数
                rf = self.racketH / h
            else:
                rf = self.racketW / w
            print('缩放系数', rf)
            racketSurface = transform.scale(self.racketSurface, (int(self.racketW / rf), int(self.racketH / rf)))
            # 球拍举行
            racketRect = racketSurface.get_rect()
            # 设置矩形中心点
            racketRect.center = centerP
            # self.window.blit(racketSurface, racketRect)
            self.racketSurfaces.append((racketSurface, racketRect))

    def showRacket(self):
        '''显示球拍'''
        # 构建球拍数据
        self.constructRacketDatas()
        # 显示到窗口上
        for ele in self.racketSurfaces:
            self.window.blit(ele[0], ele[1])

    def showBall(self):
        '''显示乒乓球'''
        # 移动矩形
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        # 保证矩形能待在屏幕内
        if self.pos_x > WINDOW_WIDTH - self.ballW:
            self.vel_x = -self.vel_x
            if self.mode==MODE.DOUBLE:
                # 左边得分
                self.leftScore += 1
        elif self.pos_x < 0:
            self.vel_x = -self.vel_x
            if self.mode == MODE.DOUBLE:
                # 右边得分
                self.rightScore += 1

        if self.pos_y > WINDOW_HEIGHT - self.ballH or self.pos_y < 0:
            self.vel_y = -self.vel_y
        # 修改小球的x和y坐标
        self.ballRect.topleft = (self.pos_x, self.pos_y)
        # 画乒乓球
        self.window.blit(self.ballSurface, self.ballRect)

    def keyDown(self, key):
        '''
        按下的事件
        :param key:按下的键
        :return:
        '''
        if key == K_SPACE:
            # 空格键 暂停
            self.isPause = not self.isPause
        elif key==K_TAB:
            BasePage.pageType=PAGETYPE.SPLASH

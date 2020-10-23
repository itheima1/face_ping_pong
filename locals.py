from enum import Enum

# 窗口网格的个数
HGRIDCOUNT = 32
VGRIDCOUNT = 24

# 网格大小
CEILSIZE = 20

# 窗口的宽度和高度
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# 定义常用颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)

ORANGE = 255,156,0
YELLOW = 255,255,0
GREENBLUE = 0,255,255
BLUE = 0,0,255
PURPLE = 255,0,255
BGCOLOR = BLACK

# 页面类型
class PAGETYPE(Enum):
    SPLASH = 0
    GAME = 1
    GAMEOVER = 2

# 游戏模式
class MODE(Enum):
    SINGLE = 0
    DOUBLE = 1
#------------------------- 图像识别 -------------------------#
# tensorflow人脸识别文件
PATH_TO_CKPT = './model/frozen_inference_graph_face.pb'

#------------------------- 小球运动的方向 -------------------------#
class Direction(Enum):
    LEFT = 0
    RIGHT = 1



# 作为一个程序猿，我是这样找回我的春天的...

啊啊啊啊啊啊啊，一起开发回春神器



程序猿和程序媛朋友们，你们有脖子疼过吗？ 

上个月我的脖子就开始偶尔作痛，我想每个人每个月都会有那么几天不舒服，脖子痛，肚子痛这不都是小毛病吗，过几天就好了。

所以偶尔的疼痛根本就没有干扰到我用心写bug，可是我万万没想到，脖子痛的time.sleep()的时间越来越短，时不时的还**头晕目眩，眼睛昏花，小手发麻**。



亚里士多德说过，身体不舒服千万别去问百度,否则你会丧失继续活下去的信心！

**我偏偏不信。**



百度之后，感觉自己的症状就是眼压升高，弄不好年纪轻轻有失明的危险。



赶紧挂个号去眼科看看吧。



见到了资深的眼科医生，医生说根据他多年的经验，你的眼没事，去拍个颈椎的片子吧。 

这个表你看看。自己对照一下级别。

| 1级  | 抬头脖子痛                 |
| ---- | -------------------------- |
| 2级  | 背酸，僵硬                 |
| 3级  | 容易落枕                   |
| 4级  | 胳膊无力，容易麻木         |
| 5级  | 走路发飘，容易跑偏         |
| 6级  | 握笔不稳，字体变化         |
| 7级  | 无法拿稳筷子               |
| 8级  | 走路一脚深，一脚浅         |
| 9级  | 大小便失禁，有一些难言之隐 |
| 10级 | 瘫痪了，下不了床           |

我好像是四级....（好像还有得救哎）

瑟瑟发抖，有木有！！



DR片子证实了医生的判断。



程序猿进阶之路我是知道的，

python语言入门 —> python语言应用实践 —> python 语言高阶编程 —> python语言的科学与艺术 —> 编程之美 —> 编程之道 —> 编程之禅—>颈椎病康复指南，

现在我直接从Python语言入门，一步跨越到了最终阶段。

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603284644104.png) 

医生看了片子之后，诡异一笑，你是个程序猿吧。



没错，我是个程序猿，可是我还没到这么高的级别呀。 o(╥﹏╥)o



医生说：你这种情况我见的多了，现在的程序猿996，每天都要坐在工位上不断写bug，而这么一坐就是一天，有时候还要加班到凌晨，没有颈椎病才怪！！



我问：你有药吗？



医生说：无药可医，不过你这个病少看电脑，多打网球，羽毛球和游泳，或者经常练习抬头，慢慢就好了。



我是行动派，回到公司，我就在某平台上找到了羽毛球和游泳馆，并查询了详细价格。

![1603284385041](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603284385041-1603430049883.png)

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603284485648-1603430049883.png)

![1603285239076](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603285239076-1603430049883.png)

看了价格后。 我毅然的选择了，自己动手治自己的病，

根据颈椎病的原理，我们只需要开发出来一款要需要大量控制脸部运动的程序即可。



颈椎病康复理疗器程序正式立项！

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603346421129.png)



图像识别python稍微方便一点， 先把python给装上，双击下一步，一路双击老铁666，python就安装好了。

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603343437820.png)

opencv是个好用的图像识别的库，那装一下把，pip install opencv-python

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603343253440.png)
好了写个代码，打开摄像头,这样就能看到画了，嘻嘻我躲在摄像头的旁边。

```python
import cv2
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret_flag, frame = cap.read()
    cv2.imshow('itheima', frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv2.destoryAllWindows()
```

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603346806491.png)

第二步识别出来我的小脸，正好opencv带有人脸的特征文件

```python
import cv2
# 加载人脸xml的特征文件
face_classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret_flag, frame = cap.read()
    # 将彩图转成灰度图
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# 调用人脸识别的api             
    faces = face_classifier.detectMultiScale(frame_gray,1.3,3);
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("itheima",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv2.destoryAllWindows()

```

一运行效果惨不忍睹，一方面是经常找不到我的脸，一方面是经常把不相干的东西当成脸识别出来。

![1603293873394](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603293873394-1603430049883.png)



没办法opencv自带的模型太差，听说mobilenet效果还行，那就用深度学习自己训练一个人脸识别的模型吧，

```
python tensorflow/examples/image_retraining/retrain.py \
    --image_dir ~/ml/face/data/ \
    --learning_rate=0.0001 \
    --testing_percentage=20 \
    --validation_percentage=20 \
    --train_batch_size=32 \
    --validation_batch_size=-1 \
    --flip_left_right True \
    --random_scale=30 \
    --random_brightness=30 \
    --eval_step_interval=100 \
    --how_many_training_steps=600 \
    --architecture mobilenet_2.0_224
```

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603294187741.png)

嗯，看训练趋势感觉效果还可以。测试一下吧。



![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603295288791.png)
嗯，效果还行，很小的头都能识别出来了，你能看出来他俩是谁吗？





好了，那用pygame做个用头控制的打乒乓球的游戏吧。

导入pygame包，再写一些简单的逻辑代码~

pygame主要是个循环，在while里面写逻辑就可以了。

```python
import pygame, sys #导包
from pygame.locals import * # 全局常量

# 初始化
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((400,270)) # 尺寸

# Surface对象
surf = pygame.Surface((50,50)) # 长、宽
surf.fill((255,255,255)) # 背景颜色

# Surface对象的矩形区域
rect = surf.get_rect()


# 窗口主循环
while True:
    # 遍历事件队列    
    for event in pygame.event.get():
       if event.type == KEYDOWN:           
            if event.key == K_ESCAPE: # 按下'ESC'键，终止主循环
                pygame.quit()
                sys.exit()                
    
    # 放置Surface对象
    screen.blit(surf, ((400-50)//2, (270-50)//2)) # 窗口正中
    #screen.blit(surf, rect)                      # surf的左上角
    
    # 重绘界面
    pygame.display.flip()
```



这点代码有点多，那我抽取出来面向对象吧，再完善一点小细节。

![1603349515763](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603349515763-1603430049883.png)





大功告成！

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603345120673.png)

![1603284485648](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/1603344458979.png)
![pingpong](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/pingpong-1603430049883.gif)



工作之余，运动后果然神清气爽，感觉我的春天回来了。可以继续高效的写bug了。O(∩_∩)O哈哈~





另外想不想学opencv和python，自己动手把上面的东西写出来， star本项目，或者请留下你的联系方式。

等我们录好课程会联系你的！



 ![img](https://raw.githubusercontent.com/itheima1/face_ping_pong/master/img/qrcode-1603430049883.ashx) 


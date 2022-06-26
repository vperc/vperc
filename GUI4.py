import pygame
from pygame.locals import *
#导入一些常用的函数和常量
import sys
#向sys模块借一个exit函数用来退出程序

background_image_filename = '33.png'
mouse_image_filename = '22.png'
#指定图像文件名称

pygame.init()
#初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((640,480),0,32)

#访问显示设备
pygame.display.set_caption("Hellow,World!")
             #加载.存储图片
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像

while True:
    # 游戏主循环
                 #来处理所有的事件，这好像打开大门让所有的人进入。
    for event in pygame.event.get():
        if event.type == QUIT: #用户按下关闭按钮
            # 接收到退出事件后退出程序
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()
           # 获得鼠标位置

    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置

    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()
    # 刷新一下画面

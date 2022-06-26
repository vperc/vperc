import pygame
from pygame.locals import *
# pygame.init()
#
# #size：元组参数，用来设置主窗口的大小
# #flags：功能标志位，表示创建的主窗口样式，比如创建全屏窗口、无边框窗口等.
# screen = pygame.display.set_mode(size=(),flags=pygame.FULLSCREEN)
# screen.blit(source,dest,area=None,special_flags=0)

#使用pygame之前必须初始化
pygame.init()
#设置主屏窗口 ；设置全屏格式：flags=pygame.FULLSCREEN
screen = pygame.display.set_mode(size=(500,400),flags=0)
#设置窗口标题
pygame.display.set_caption('c语言中文网')
image = pygame.image.load("hubble_hh34_potw2210a_0.png").convert()

image.fill((0,0,255),rect=(100,100,100,50),special_flags=0)
image.scroll(100,50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # 将图像放置在主屏幕上
    screen.blit(image,(0,0))
    pygame.display.update()


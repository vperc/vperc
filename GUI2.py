import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800
# 初始化
pygame.init()
# 构建游戏窗口
chuangkou = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# 设置游戏标题
pygame.display.set_caption('图片')
# 填充背景
chuangkou.fill((255, 255, 255))
pygame.display.flip()
image = pygame.image.load('hubble_hh34_potw2210a_0.png')
# 在窗口上渲染图像
chuangkou.blit(image, (50, 50))
pygame.display.update()  # 再次刷新

num = 1
d = 0  # 初始化旋转的角度
# 开启一个事件循环处理发生的事件
while True:
    num += 1
    if num % 20 == 0:
        d += 2
        newimage = pygame.transform.rotozoom(image, d, 0.2)
        chuangkou.blit(newimage, (0, 0))
        pygame.display.update()

    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            exit()
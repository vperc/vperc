import sys, pygame
from random import *
class MyClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)        #初始化动画精灵
        self.image = pygame.image.load(image_file) #加载图片
        self.rect = self.image.get_rect()          #得到定义图像边界矩形
        self.rect.left, self.rect.top = location   #设置球的初始位置
        self.speed = speed                         #创建一个速度
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
def animate(group):
    screen.fill([255, 255, 255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)      #从组删除精灵
        #检查精灵与组的碰撞
        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        group.add(ball)
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)
#设置窗口大小和颜色
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "hubble_hh34_potw2210a_0.png"
clock = pygame.time.Clock()
group = pygame.sprite.Group()   #创建精灵组
#将球增加到列表
for row in range(0, 2):
    for column in range(0, 2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-4, 4]), choice([-4, 4])]     #让每个球变得随机性
        ball = MyClass(img_file, location, speed)
        group.add(ball)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()
            print( "frame rate = ", frame_rate)
    animate(group)
    clock.tick(30)
pygame.quit()
#1.在游戏窗口中绘图
import pygame  # 导入pygame模块


def main():
    # 初始化pygame模块
    pygame.init()
    # 初始化显示窗口并设置窗口尺寸
    screen = pygame.display.set_mode((888, 666))
    # 设置当前窗口的标题
    pygame.display.set_caption('888666')
    # 设置窗口背景色
    screen.fill((255, 255, 255))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0), (444, 333), 50, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()

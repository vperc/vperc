import numpy as np
from PIL import Image
import matplotlib.pyplot as plt #绘图库

def set_chinese(): #中文显示工具函数
    import matplotlib
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

def image_inverse(input):
    value_max = np.max(input) #求输入图像的最大灰度值
    output = value_max - input
    return output

if __name__ == '__main__':
    set_chinese()
    gray_img = np.asarray(Image.open('X.jpg').convert('L'))
    inv_img = image_inverse(gray_img)

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.set_title('原图')
    ax1.imshow(gray_img,cmap='gray',vmin=0,vmax=255)

    ax2 = fig.add_subplot(122)
    ax2.set_title('反转变换结果')
    ax2.imshow(inv_img,cmap='gray',vmin=0,vmax=255)

    plt.show()

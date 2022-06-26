from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

#浏览器进入百度网址
driver.get("https://www.baidu.com")

#设置浏览器宽，高
driver.set_window_size(1600,1600)

#等待1秒
sleep(1)

#刷新界面
driver.refresh()

#等待1秒
sleep(1)

#最大化窗口
driver.maximize_window()

driver.get("https://www.lanqiao.cn/")
sleep(3)

# 后退到上一个页面--百度网站
driver.back()

sleep(3)

# 前进到下一个页面--实验楼网站
driver.forward()
sleep(3)

#退出浏览器
driver.quit()


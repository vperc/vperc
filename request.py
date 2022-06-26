import urllib.request
import time
#请求网页并获取网络用于获取请求页面的时间
ts = time.time()
req = urllib.request.urlopen("http://www.yiibai.com")
pageHtml = req.read()
te = time.time()
print("Page Fetching Time: {} Seconds".format((te-ts)))

#Python线程有时称为轻量级进程，因为线程比进程占用的内存少得多。
# 线程允许一次执行多个任务。 在Python中，以下两个模块在一个程序中实现线程
#_thread模块将线程视为一个函数，而threading模块将每个线程视为一个对象并以面向对象的方式实现它。
#_thread模块在低级线程中有效并且比threading模块具有更少的功能。
#在Python 3中，thread模块不再可用。 它已被重命名为_thread，用于Python3中的向后不兼容。
#_thread调用start_new_thread方法



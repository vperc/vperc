# -*- coding:utf-8 -*-
#交换两个变量值
#该方法是我们最常见的方法，也是最容易理解的方法，通过添加新的中间变量的方法实现交换数值
# def demo1(a,b):
#     temp = a
#     a = b
#     b = temp
#     print(a,b)
# demo1(11,22)
#方法二：
#此方法是python中特有的方法，一行代码就可以解决问题，非常快捷。是将变量放到元组中，再通过元组按照index进行赋值的方式对变量进行重新赋值
# a = 11
# b = 22
# a,b = b,a
# print(a,b) #当然这种方法并不受限于两个变量，多个变量也是可以的，只是要对应好哪个变量与哪个变量交换值
# a = 11
# b = 22
# c = 33
# a,b,c = b,c,a
# print(a,b,c)
#方法三：
#通过简单的逻辑运算进行两个值的计算，这个方法想到的同学就会少一些了，这种方法只是效率低了点，但仍能实现交换的效果
# def swap_only_ab(a,b):
#     a = a + b
#     b = a - b
#     a = a - b
#     global gl_num
#     gl_num = 2
#     return a,b
#方法四：
#通过异或运算，将两个值进行互换，能想到这种方法的同学更是少之又少。
#异或运算简单点来说就是计算机会先把十进制数转化为二进制数，并且对二进制数进行从右到左进行比较，如果比较的两个二进制数相同，结果为0，不同结果为1，1^1=0，1^0=1，0^0=0。
# a = 11
# b = 22
# a = a^b #a=11^22
# b = b^a #b=11^22^22=11^0=11
# a = a^b #a=11^22^11=22
# print(a,b)
#可使用于加密算法某一环节或更多环节，使算法更复杂，不易被破解，安全性更高。
# 摄氏度与华氏度的转换%
# c = float(input("请输入你要输入的摄氏温度："))
# f = c*1.8+32
# print("对应的华氏温度为：%.1f"%f)
#
# f = float(input("请输入你要输入的华氏温度："))
# c = 5.0/9.0*(f-32)
# print("对应的摄氏度温度为：%.1f"%f)
# #用python计算整数各位数字之和
# n = input("请输入你要输入的数：")  #将数字作为字符串输入
# list = list(n) #将字符串转换为列表
# print(list)
# print(len(list))
# s = 0
# for i in range(len(list)):
#     s +=int(list[i]) #将字符转化为整数型,并累加列表中的每一个数字
#     print(i)
# print(s)
#判断一个数是否为素数
# 运用python的数学函数
# import math
# def isPrime(n):
#     if n <= 1:
#         return False #事件处理函数会取消事件，不再继续向下执行,表单将终止提交
#     for i in range(2,int(math.sqrt(n))+ 1):
#         if n % i == 0:
#             return False
#         return True
# 单行程序扫描素数
# from math import sqrt
# N = 100
# [ p for p in range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]
#运用python的itertools模块
# from itertools import count
# def isPrime(n):
#     if n <=1:
#         return False
#     for i in count(2):
#         if i * i > n:
#             return True
#         if n % i == 0:
#             return False
#不使用模块的两种方法
#方法一:
# def isPrime(n):
#     if n <= 1:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True
# #方法二:
# def isPrime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 2
#     return True
#Python产生随机数方法
#一.Python自带的random库
# 1.参生n–m范围内的一个随机数: random.randint(n,m)
# 2. 产生0到1之间的浮点数: random.random()
# 3.产生n - --m之间的浮点数: random.uniform(1.1, 5.4)
# 4.产生从n - --m间隔为k的整数: random.randrange(n, m, k)
# 5.从序列中随机选取一个元素: random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
#6. 在一些特殊的情况下可能对序列进行一次打乱操作: random.shuffle([1, 3, 5, 6, 7])
# import random
# # 产生 1 到 10 的一个整数型随机数
# print(random.randint(1, 10))
# # 产生 0 到 1 之间的随机浮点数
# print(random.random())
# # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print(random.uniform(1.1, 5.4))
# # 从序列中随机选取一个元素
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# # 生成从1到100的间隔为2的随机整数
# print(random.randrange(1, 100, 2))
# # 将序列a中的元素顺序打乱
# a = [1, 3, 5, 6, 7]
# random.shuffle([1, 3, 5, 6, 7])
# print(a)
# import random
# a = random.randint(1,100)
# print(a)
# b = random.uniform(1,10)
# print("%.2f"%b)
#删除列表中重复元素
#1. 使用内置函数set
# lists = [1,1,2,3,4,6,6,2,2,9]
# lists = list(set(lists))
# print(lists)
#先将列表转换为集合，因为集合是不重复的，故直接删除重复元素
#2.使用del函数或者remove函数
# lists = [1,1,2,3,4,6,9,6,2,2]
# lists.sort()
# t = lists[-1]
# for i in range(len(lists)-2,-1,-1):
#     if t == lists[i]:
#         lists.remove(lists[i])
#     else:
#         t = lists[i]
#使用这种方法时需要先进行排序，然后对比相邻两个元素是否相同，相同即删除。
# 这里只能从lists[-1]开始进行循环，因为从0开始后，在进行删除元素时列表长度会发生改变，造成列表越界。从后往前开始则不会出现此问题。
#3. numpy.unique()方法去重
# import numpy as np
# lists = [1,1,2,3,4,6,9,6,2,2]
# lists = np.unique(lists)
# print(lists)
#在科学计算库numpy中有一个方法来进行去重，但返回结果为ndarray类型


#反转一个字符串（回文检测）
#Python没有任何内置函数来反转字符串
#定义自定义函数并使用它来反转字符串：
# def rev_str_thru_slicing(str_):
#     return  str_[::-1]
#
# INPUT_STRING = "Linuxize"
#
# if __name__ == '__main__': # 语句之前和之后的代码都被执行。判断是否执行正确 隐私不能被导入 #假如你叫小明.py，在朋友眼中，你是小明(_name_ == '小明')；
# # 在你自己眼中，你是你自己(_name_ == '_main_')。if _name_ == '_main_'之下的代码块可以理解为小明的隐私，在自己程序里隐私可以被看到，在被他人引用时则看不到。
#     print("INPUT STRING -", INPUT_STRING)
#     print("REVERSED STRING -", rev_str_thru_slicing(INPUT_STRING))
#使用reversed()功能
#内置reserved()函数以相反的顺序处理字符串项并返回一个反向迭代器。在下面的示例中，使用运算符将反向迭代器的元素添加到空字符串中join()：
# def rev_str_thru_join_revd(STR):
#     return "".join(reversed(STR))
#
# INPUT_STRING = "Linuxize"
#
# if __name__ == '__main__':
#     print("INPUT STRING -", INPUT_STRING)
#     print("REVERSED STRING -", rev_str_thru_slicing(INPUT_STRING))
#使用列表reverse()
#要使用list 方法反转字符串reverse()，首先需要使用list构造函数将字符串转换为列表，然后使用该方法将列表项反转到位reverse()，最后使用该方法将列表项连接成一个字符串join()。
# def rev_str_thru_list_reverse(STR):
#     lsl = list(STR)
#     lsl.reverse()
#     return (''.join(lsl))
# INPUT_STRING = "Linuxize"
# if __name__ == '__main__':
#     print("INPUT STRING -", INPUT_STRING)
#     print("Reserved String Through List", rev_str_thru_list_reverse(INPUT_STRING))
#使用递归函数
#在下面的代码片段中，rev_str_thru_recursion函数调用自身，直到字符串长度大于零。每次调用时，都会对字符串进行切片，只留下第一个字符。稍后，它与切片字符连接。
# def rev_str_thru_recursion(STR):
#     if len(STR) == 0:
#          return STR
#     else:
#         return rev_str_thru_recursion(STR[1:]) + STR[0]
#
# INPUT_STRING = "Linuxize"
#
# if __name__ == '__main__':
#     print("INPUT STRING -", INPUT_STRING)
#
# print("RESERVED STRING THROUGH RECURSION", rev_str_thru_recursion(INPUT_STRING))
#计算最大公约数
#方法一：辗转相除法
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字: "))
# m = max(num1,num2)
# n = min(num1,num2)
# r = m % n
# while r!=0:
#     m = n
#     n = r
#     r = m % n
# print(num1, "和", num2, "的公约数为", n)
#方法二：辗转相减法
# def fuc2(p, q):
#     while p!=q:
#         if p>q:
#             p = p - q
#         else:
#             q = q - p
#     return p
#方法三：枚举法
# def fun3(a, b):
#     p = a * b
#     t = a  # 将a值赋给t
#     while t > 0:
#         if a % t == 0 and b % t == 0:  # 若a除以t的余数和b除以t的余数都为0时，跳出循环
#             break
#         t = t - 1  # t>0时，每循环一次，t值减一
#     print("枚举法得公约数为：", t)  # 当跳出循环时，输出t值即为公约数
# # 用枚举法求三个正整数的公约数
# def fun4(a, b, c):
#     p = a * b * c
#     if a < b:
#         min = a
#     else:
#         min = b
#         if min > c:
#             min = c  # 找出输入的a,b,c三个数中的最小的数赋给min
#     while min > 0:
#         if a % min == 0 and b % min == 0 and c % min == 0:  # 若a除以的余数和b除以min的余数和c除以min都为0时，跳出循环
#             break
#         min = min - 1  # >0时，每循环一次，min值减一
#     print("枚举法得三个数的公约数为：", min)  # 当跳出循环时，输出min值即为公约数
#合并两个有序数组
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         if n == 0:
#             return nums1  # 特殊情况
#
#         for i in range(m, m + n):
#             nums1[i] = nums2[i - m]  # 赋值
#
#         nums1.sort()  # 排序
#         return nums1
# class Solution():
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         index = m + n - 1  # 合并之后的nums1最大的下标
#         # 个数减去1得到下标
#         m -= 1
#         n -= 1
#         while m >= 0 and n >= 0:
#             # 如果nums1倒数最大 大于nums2倒数最大
#             # 第一轮nums1的5和nums2的6
#             # 第二轮nums1的5和nums2的4比较
#             if nums1[m] > nums2[n]:
#                 # nums1的5放到
#                 nums1[index] = nums1[m]
#                 #比nums1较下一个
#                 m -= 1
#             else:
#                 # 第一轮的nums2的6放到nums1的最后
#                 nums1[index] = nums2[n]
#                 # 比较nums2的下一个
#                 n -= 1
#             # 最大索引减一放剩下数组里的大数
#             index -= 1
#         if m < 0:
#             #说明nums1的数都大于nums2
#             nums1[:n + 1] = nums2[:n + 1]
#
# if __name__ == '__main__':
#     nums1 = [1, 3, 4, 5, 0, 0, 0]
#     nums2 = [2, 4, 6]
#     s = Solution()
#     s.merge(nums1, 4, nums2, 3)
#     print(nums1)
#猜数字游戏
# coding:utf-8
# import random
#
# cmp = random.randint(0, 999)
# time = 1
# small = 0
# big = 999
# answer = int(input("Input your answer(%d-%d): " % (small, big)))
# while answer != cmp:
#     time += 1
#     if answer > cmp:
#         print("Your answer is big")
#         if answer > big:
#             big = big
#         else:
#             big = answer
#         answer = int(input("Input your answer(%d-%d): " % (small, big)))
#     else:
#         print("Your answer is small")
#         if answer < small:
#             small = small
#         else:
#             small = answer
#         answer = int(input("Input your answer(%d-%d): " % (small, big)))
# print("The answer is %d. You get it by %d times" % (cmp, time))
#计算年龄
# import time
#
# now = time.strftime('%Y%m%d',time.localtime(time.time()))
# bday = input("insert birthday example:20170101:")
# def getDays( year, month ):
#     day = 31
#     while day:
#         try:
#             time.strptime( '%s-%s-%d'%( year, month, day ), '%Y-%m-%d' )
#             return day
#         except:
#             day -= 1
#
# mons = list(range(1,13))
# if (bday[4]) == '0':
#     monn = bday[5:6]
# else:
#     monn = bday[4:6]
#
# if (now[4]) == '0':
#     mon_now = now[5:6]
# else:
#     mon_now = now[4:6]
#
# youxm = mons[int(monn):int(mon_now)-1]
# monns = 0
# if (int(now[0:4]) - int(bday[0:4])) == 0:
#     for monss in youxm:
#         monns = int(monns) + int(getDays(int(bday[0:4]), int(monss)))
#     monns = int(getDays(int(bday[0:4]), int(monn))) -int(bday[6:9]) + int(now[6:9]) + 1 +monns
# elif (int(now[0:4]) - int(bday[0:4])) == 1:
#     youxm = mons[int(monn):13]
#     for monss in youxm:
#         monns = int(monns) + int(getDays(int(bday[0:4]), int(monss)))
#     monns = monns + int(getDays(int(bday[0:4]), int(monn))) -int(bday[6:9])+1
#     youxm = mons[0:int(mon_now)-1]
#     for monns_now in youxm:
#         monns = int(monns) + int(getDays(int(now[0:4]), int(monns_now)))
#     monns = monns + int(now[6:9])
# else:
#     youxms = list(range(int(bday[0:4])+1,int(now[0:4])))
#     monns = 0
#     for youxm in youxms:
#         for monsz in mons:
#             monns = int(monns) + int(getDays(int(youxm), int(monsz)))
#     youxm = mons[int(monn):13]
#     for monss in youxm:
#         monns = int(monns) + int(getDays(int(bday[0:4]), int(monss)))
#     monns = monns + int(getDays(int(bday[0:4]), int(monn))) -int(bday[6:9])+1
#     youxm = mons[0:int(mon_now)-1]
#     for monns_now in youxm:
#         monns = int(monns) + int(getDays(int(now[0:4]), int(monns_now)))
#     monns = monns + int(now[6:9])
# year = monns//365
# days = monns%365
# if monns < 365*5:
#     print('宝宝年龄是' + str(year) + '岁' + str(days) + '天')
# else:
#     print('您的年龄是'+str(year)+'岁'+str(days)+'天')
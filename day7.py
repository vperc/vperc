#两个查找算法—线性查找和二分查找
#什么叫查找
#查找:在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程。列表查找(线性表查找):从列表中查找指定元素
#输入:列表、待查找元素 输出:元素下表(未找到元素时一般返回None或-1) 内置列表查找函数:index()
#顺序查找(Linea Search) 顺序查找:也叫作线性查找，从列表第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止
#1.顺序查找(Linea Search)
#顺序查找代码
# def linear_search(li,val):
#     for index,value in enumerate(li):
#         if value == val:
#             return  index
#         else:
#             return None
# #时间复杂度为O(n) 顺序查找是把列表从头到尾查找一遍，最多找n次
# #2.二分查找(Binary Search)
# #二分查找需要事先排序
# def binary_search(li,val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val:  #待查找的值在mid左侧
#             right = mid - 1
#         else: #li[mid]<val   待查找的值在mid右边侧
#             left = mid + 1
#     else:
#         return None
# li = [1,2,3,4,5,6,7,8,9]
# print(binary_search(li, 3))
#二分查找的复杂度O(logn)
#列表的内置函数index()实现的是线性查找方式，二分查找要求列表必须是有序列表，二分查找速度快，但是必须排序。排序的时间复杂度大于O(n)。
#需要查找时，若实现有序则优先使用二分查找，无序则要考虑排序。若排序后查找次数很少，则不如使用线性查找(因为要考虑排序时间)，但是若要多次使用查找，则可以先排序。
#冒泡排序
#冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
# def mao(lst):
#     for i in range(len(lst)):
#         # 由于每一轮结束后，总一定有一个大的数排在后面
#         # 而且后面的数已经排好了
#         # 即i轮之后，就有i个数字被排好
#         # 所以其 len-1 -i到 len-1的位置是已经排好的了
#         # 只需要比较0到len -1 -i的位置即可
#
#         # flag 用于标记是否刚开始就是排好的数据
#         # 只有当flag状态发生改变时（第一次循环就可以确定），继续排序，否则返回
#         flag = False
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 flag = True
#                 # 非排好的数据，改变flag
#         if not flag:
#             return lst
#     return lst
#
# print(mao([1, 5, 55, 4, 5, 1, 3, 4, 5, 8, 62, 7]))
#选择排序
#选择排序是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
# 选择排序是从前开始排的
# 选择排序是从一个列表中找出一个最小的元素，然后放在第一位上。
# 冒泡排序类似
# 其 0 到 i的位置是排好的，只需要排i+1到len(lst)-1即可

# def select_sort(lst):
#     for i in range(len(lst)):
#         min_index = i  # 用于记录最小的元素的索引
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#
#         # 此时，已经确定，min_index为 i+1 到len(lst) - 1 这个区间最小值的索引
#         lst[i], lst[min_index] = lst[min_index], lst[i]
#
#     return lst
#
#
# def select_sort2(lst):
#     # 第二种选择排序的方法
#     # 原理与第一种一样
#     # 不过不需要引用中间变量min_index
#     # 只需要找到索引i后面的i+1到len(lst)的元素即可
#
#     for i in range(len(lst)):
#         for j in range(len(lst) - i):
#
#             # lst[i + j]是一个i到len(lst)-1的一个数
#             # 因为j <= len(lst) -i 即 j + i <= len(lst)
#             if lst[i] > lst[i + j]:
#                 # 说明后面的数更小，更换位置
#                 lst[i], lst[i + j] = lst[i + j], lst[i]
#     return lst
#
#
# print(select_sort([1, 5, 55, 4, 5, 1, 3, 4, 5, 8, 62, 7]))
# print(select_sort2([1, 5, 55, 4, 5, 1, 3, 4, 5, 8, 62, 7]))
#快速排序
#快速排序是通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
# 原理
# 1. 任取列表中的一个元素i
# 2. 把列表中大于i的元素放于其右边，小于则放于其左边
# 3. 如此重复
# 4. 直到不能在分，即只剩1个元素了
# 5. 然后将这些结果组合起来
# def quicksort(lst):
#     if len(lst) < 2:    # lst有可能为空
#         return lst
#
#     # ['pɪvət] 中心点
#     pivot = lst[0]
#     less_lst = [i for i in lst[1:] if i <= pivot]
#     greater_lst = [i for i in lst[1:] if i > pivot]
#     # 最后的结果就是
#     #           左边的结果 + 中间值 + 右边的结果
#     # 然后细分   左+中+右   + 中间值 + 左 + 中+ 右
#     #      ...........    + 中间值 + ............
#     return quicksort(less_lst) + [pivot] + quicksort(greater_lst)
#
#
# print(quicksort([1, 5, 55, 4, 5, 1, 3, 4, 5, 8, 62, 7]))
# print(quicksort([1, 5, 8, 62]))
#插入排序
#插入排序的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# lst的[0, i) 项是有序的，因为已经排过了
# 那么只需要比对第i项的lst[i]和lst[0 : i]的元素大小即可
# 假如，lst[i]大，则不用改变位置
#     否则，lst[i]改变位置，插到j的位置，而lst[j]自然往后挪一位
#     然后再删除lst[i+1]即可（lst[i+1]是原来的lst[i]）
#
# 重复上面步骤即可，排序完成
# def insert_sort(lst: list):
#     # 外层开始的位置从1开始，因为从0开始都没得排
#     # 只有两个元素以上才能排序
#     for i in range(1, len(lst)):
#         # 内层需要从0开始，因为lst[0]的位置不一定是最小的
#         for j in range(i):
#             if lst[i] < lst[j]:
#                 lst.insert(j, lst[i])
#                 # lst[i]已经插入到j的位置了，j之后的元素都往后+1位，所以删除lst[i+1]
#                 del lst[i + 1]
#     return lst
# print(insert_sort([1, 5, 55, 4, 5, 1, 3, 4, 5, 8, 62, 7]))
#希尔排序
# 作者：沙振宇
# 希尔排序
# def shellSort(arr):
#   import math
#   gap=1
#   while(gap < len(arr)/3):
#     gap = gap*3+1
#   while gap > 0:
#     for i in range(gap,len(arr)):
#       temp = arr[i]
#       j = i-gap
#       while j >=0 and arr[j] > temp:
#         arr[j+gap]=arr[j]
#         j-=gap
#       arr[j+gap] = temp
#     gap = math.floor(gap/3)
#   return arr
# if __name__ == '__main__':
#   list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#   print("List source is:", list)
#   result = shellSort(list)
#   print("List sort is:", result)
#归并排序
# 作者：沙振宇
# 归并排序
# def mergeSort(arr):
#   import math
#   if(len(arr)<2):
#     return arr
#   middle = math.floor(len(arr)/2)
#   left, right = arr[0:middle], arr[middle:]
#   return merge(mergeSort(left), mergeSort(right))
# def merge(left,right):
#   result = []
#   while left and right:
#     if left[0] <= right[0]:
#       result.append(left.pop(0))
#     else:
#       result.append(right.pop(0))
#   while left:
#     result.append(left.pop(0))
#   while right:
#     result.append(right.pop(0))
#   return result
# if __name__ == '__main__':
#   list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#   print("List source is:", list)
#   result = mergeSort(list)
#   print("List sort is:", result)
#计数排序
# 作者：沙振宇
# 计数排序
# def countingSort(arr, maxValue):
#   bucketLen = maxValue+1
#   bucket = [0]*bucketLen
#   sortedIndex =0
#   arrLen = len(arr)
#   for i in range(arrLen):
#     if not bucket[arr[i]]:
#       bucket[arr[i]]=0
#     bucket[arr[i]]+=1
#   for j in range(bucketLen):
#     while bucket[j]>0:
#       arr[sortedIndex] = j
#       sortedIndex+=1
#       bucket[j]-=1
#   return arr
# if __name__ == '__main__':
#   list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#   print("List source is:", list)
#   result = countingSort(list,max(list))
#   print("List sort is:", result)
#基数排序
# 作者：沙振宇
# 基数排序
# def radix_sort(arr):
#   """基数排序"""
#   i = 0 # 记录当前正在排拿一位，最低位为1
#   max_num = max(arr) # 最大值
#   j = len(str(max_num)) # 记录最大值的位数
#   while i < j:
#     bucket_list =[[] for _ in range(10)] #初始化桶数组
#     for x in arr:
#       bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
#     arr.clear()
#     for x in bucket_list:  # 放回原序列
#       for y in x:
#         arr.append(y)
#     i += 1
#   return arr
# if __name__ == '__main__':
#   list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#   print("List source is:", list)
#   result = radix_sort(list)
#   print("List sort is:", result)
#桶排序
# 作者：沙振宇
# 桶排序
# def bucketSort(arr):
#   # 选择一个最大的数
#   max_num = max(arr)
#   # 创建一个元素全是0的列表, 当做桶
#   bucket = [0] * (max_num + 1)
#   # 把所有元素放入桶中, 即把对应元素个数加一
#   for i in arr:
#     bucket[i] += 1
#   # 存储排序好的元素
#   sort_nums = []
#   # 取出桶中的元素
#   for j in range(len(bucket)):
#     if bucket[j] != 0:
#       for y in range(bucket[j]):
#         sort_nums.append(j)
#   return sort_nums
# if __name__ == '__main__':
#   list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#   print("List source is:", list)
#   result = bucketSort(list)
#   print("List sort is:", result)
#递归函数
#递归求和:可以利用递归函数实现一个Python内置函数sum()的递归版。
#递归
# 递归
# def d_sum(L):
#   if not L:
#     return 0
#   else:
#     return L[0] + d_sum(L[1:])
# sum_l = d_sum(range(10))
# print(sum_l)
#该递归函数怎么实现列表元素相加的呢？ 我们知道函数是有本地作用域的，对函数调用的每一个打开的时候，
#在运行时调用堆栈上都有自己的一个本地作用域的副本，即L在每个层级都是不同的，比如我们可以通过每次调用时添加一个打印语句，更加直观展示每个层级L的情况
#递归
# def d_sum(L):
#     print(L)
#     if not L:
#       return 0
#     else:
#       return L[0] + d_sum(L[1:])
# #构建 0-10 数字元素列表
# L = [i for i in range(100)]
# sum_l = d_sum(L)
# print(sum_l)
#处理任意结构
#比如我们可以利用递归计算一个嵌套的子列表结构中所有数字的总和
# def dd_sum(L):
#   tot = 0
#   for x in L:
#     if not isinstance(x, list):
#       tot += x
#     else:
#       tot += dd_sum(x)
#   return tot
#
# # 嵌套列表
# L = [1,[2,3],[4,[5,6,7],8],9]
# sum_l = dd_sum(L)
# print(sum_l)
#递归的使用
#1.求阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
#2.
# import math
# print(math.factorial(5))
#2、汉诺塔
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
# def move(n,a,b,c):
#     if n == 1:
#         print(a,'-->',c)
#     else:
# #将n-1个盘子从a移动到b上
#         move(n-1,a,c,b)
#         print(a,'-->',c)
#         move(n-1,b,a,c)
#
# move(3,'A','B','C')
# #3、斐波那契数列
# # Fibonacci数列为：0、1、1、2、3、5、8、13、21......数列第一项为0，第二项为1，从第三项开始，每一项为相邻前两项之和。 用递归的方法来定义：
# def f(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return  f(n-1)+f(n-2)
# print(f(5))
#时间复杂度
# def linear_search(l, x):  # 线性搜索 列表的长度是决定性因素 O(len(l))
#     for e in l:
#         if e == x:
#             return True
#         return False
#线性搜索的时间复杂度O(n)，取决于列表的长度，在时间复杂度上来说它是一种优秀复杂度，因为随着列表的增长，时间复杂度不会出现爆炸性的增长。
#递归、单层循环
# def fact(n):
#     answer = 1  # 1
#     while n > 1:  # 5 *n
#         answer *= n
#         n -= 1
#     return answer  # 1   所有 5n + 2

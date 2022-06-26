# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# f()
#
# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))
#
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# 5.数据结构
# list.append(x)
# #在列表的末尾添加一个元素。相当于 a[len(a):] = [x]
#
# list.extend(iterable)
# #使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable
#
# list.insert(i, x)
# #a.insert(len(a), x) 等同于 a.append(x)
#
# list.remove(x)
# #移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常
#
# list.pop([i])
# #删除列表中给定位置的元素并返回它
#
# list.clear()
# #移除列表中的所有元素。等价于``del a[:]``
#
# #list.index(x[, start[, end]])
# #返回列表中第一个值为 x 的元素的从零开始的索引。如果没有这样的元素将会抛出 ValueError 异常
#
# count(x)
# #返回元素 x 在列表中出现的次数。
#
# #list.sort(*, key=None, reverse=False)
# #对列表中的元素进行排序（参数可用于自定义排序，解释请参见 sorted()）
#
# list.reverse()
# #翻转列表中的元素
#
# list.copy()
# #返回列表的一个浅拷贝，等价于 a[:]

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')
# fruits.count('tangerine')
# fruits.index('banana')
# fruits.index('banana', 4)
# fruits.reverse()
# fruits.append('grape')
# fruits.sort()#对列表进行排序
# fruits.pop()

#5.1.1. 列表作为栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()#从栈的顶部取出一个元素
stack.pop()
stack.pop()
stack.pop()
print(stack)

#5.1.2. 列表作为队列使用
#若要实现一个队列，可使用 collections.deque，它被设计成可以快速地从两端添加或弹出元素
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

#5.1.3. 列表推导式
#创建一个平方列表
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
#这将创建（或覆盖）一个名为 x 的变量，该变量在循环结束后仍然存在。 下述方法可以无副作用地计算平方列表:
squares = [x**2 for x in range(10)] #等价于squares = list(map(lambda x: x**2, range(10)))

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
            print(combs)
#如果表达式是一个元组（例如上面的 (x, y)），那么就必须加上括号
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
#5.1.4. 嵌套的列表推导式
#列表推导式中的初始表达式可以是任何表达式，包括另一个列表推导式。考虑下面这个 3x4的矩阵，它由3个长度为4的列表组成。
matrix = [
       [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
         ]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
      transposed.append([row[i] for row in matrix])
      print(transposed)
#实际应用中，你应该会更喜欢使用内置函数去组成复杂的流程语句。 zip() 函数将会很好地处理这种情况
print(list(zip(*matrix)))

#5.2. del 语句
# del 语句也可以用来从列表中移除切片或者清空整个列表
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
del a[:]
print(a)

#5.3. 元组和序列
#我们看到列表和字符串有很多共同特性，例如索引和切片操作。他们是 序列 数据类型
t = 12345, 54321, 'hello!'
print(t[0])

empty = ()
singleton = 'hello',
len(empty)
len(singleton)
print(singleton)

#5.4. 集合
#它的基本用法包括成员检测和消除重复元素。集合对象也支持像 联合，交集，差集，对称差分等数学运算。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print( a - b )
print(a | b )
print(a & b  )
print(a ^ b   )
#类似于 列表推导式，集合也支持推导式形式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#5.5. 字典
#字典在其他语言里可能会被叫做 联合内存 或 联合数组。与以连续整数为索引的序列不同，字典是以 关键字 为索引的，关键字可以是任意不可变类型，通常是字符串或数字。
# 如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。
# 但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字。列表不能用作关键字，因为列表可以通过索引、切片或 append() 和 extend() 之类的方法来改变。

tel = {'jack': 4098, 'sape': 4139}#定义了一个字典
tel['guido'] = 4127

#循环的技巧
knights = {'gallahad': 'the pure', 'robin': 'the brave'}#当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出
for k,v in knights.items():
    print(k,v)

#当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配。
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#如果要逆向循环一个序列，可以先正向定位序列，然后调用 reversed() 函数
for i in reversed(range(1, 15, 3)):
    print(i)
#如果要按某个指定顺序循环一个序列，可以用 sorted() 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#有时可能会想在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

#5.7. 深入条件控制
#也可以把比较操作或者逻辑表达式的结果赋值给一个变量
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

#6.1.2. 模块搜索路径
#当一个名为 spam 的模块被导入的时候，解释器首先寻找具有该名称的内置模块。
# 如果没有找到，然后解释器从 sys.path 变量给出的目录列表里寻找名为 spam.py 的文件。sys.path 初始有这些目录地址:

# #6.2. 标准模块
# import sys
# print(sys.ps1)
# print(sys.ps2)
# sys.ps1 = 'C> '
# print('Yuck!')
#
# #sys.path 变量是一个字符串列表，用于确定解释器的模块搜索路径。
# # 该变量被初始化为从环境变量 PYTHONPATH 获取的默认路径，或者如果 PYTHONPATH 未设置，则从内置默认路径初始化。
# # 你可以使用标准列表操作对其进行修改:
# # import sys
# # sys.path.append('/ufs/guido/lib/python')
#
# #6.3. dir() 函数
# #内置函数 dir() 用于查找模块定义的名称。 它返回一个排序过的字符串列表:
# import fibo, sys
# print(dir(fibo))
# print(dir(sys))

#6.4. 包
#包是一种通过用“带点号的模块名”来构造 Python 模块命名空间的方法。
# 例如，模块名 A.B 表示 A 包中名为 B 的子模块。
# 正如模块的使用使得不同模块的作者不必担心彼此的全局变量名称一样。
# 使用加点的模块名可以使得 NumPy 或 Pillow 等多模块软件包的作者不必担心彼此的模块名称一样。

#7. 输入输出
# 有几种方法可以显示程序的输出；数据可以以人类可读的形式打印出来，或者写入文件以供将来使用。本章将讨论一些可能性。
#7.1. 更漂亮的输出格式
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
#str() 函数是用于返回人类可读的值的表示，而 repr() 是用于生成解释器可读的表示（如果没有等效的语法，
# 则会强制执行 SyntaxError）对于没有人类可读性的表示的对象， str() 将返回和 repr() 一样的值。
# 很多值使用任一函数都具有相同的表示，比如数字或类似列表和字典的结构。特殊的是字符串有两个不同的表示。
s = 'hello,world'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
repr((x, y, ('spam', 'eggs')))
#7.1.1. 格式化字符串文字
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# #7.1.2. 字符串的 format() 方法
# #str.format() 方法的基本用法如下所示:
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# #花括号和其中的字符（称为格式字段）将替换为传递给 str.format() 方法的对象。花括号中的数字可用来表示传递给 str.format() 方法的对象的位置。
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

#8. 错误和异常
#9. 类

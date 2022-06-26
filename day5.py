#Python 实现栈
#栈的抽象数据结构
#栈是有序的LIFO(后进先出)。
#栈的操作有：Stack() 创建新的空栈。push(item) 添加新项到栈顶部。pop() 删除栈顶项并返回栈顶项的值。栈被修改。peek() 返回栈顶部项。不修改栈。
# isEmpty() 测试栈是否为空，返回 Bool 值。size() 返回栈长度（栈中 item 数量）。
#利用列表实现栈
# class Stack:
#     def __init__(self): #当我们创建好一个对象后，实例化对象。
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
# if __name__ == '__main__':
#     s = Stack()
#     print(s.isEmpty())
#     s.push(4)
#     s.push('dog')
#     print(s.peek())
#     s.push(True)
#     print(s.size())
#     print(s.isEmpty())
#     s.push(8.4)
#     print(s.pop())
#     print(s.pop())
#     print(s.size())
#简单括号匹配
#区分括号是否匹配的能力是识别很多编程语言结构的重要部分。具有挑战的是如何编写一个算法，能够从左到右读取一串符号，并决定符号是否平衡。
# 为了解决这个问题，我们需要做一个重要的观察。从左到右处理符号时，最近开始符号必须与下一个关闭符号相匹配(见 Figure 1)。此外，处理的第一个开始符号必须等待直到其匹配最后一个符号。结束符号以相反的顺序匹配开始符号。他们从内到外匹配。这是一个可以用栈解决问题的线索。
#括号匹配
# def parChecker(symbol_sring):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbol_sring) and balanced:
#         symbol = symbol_sring[index]
#         if symbol == '(':
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()
#             index += 1
#
#             if balanced and s.isEmpty():
#                 return True
#             else:
#                 return False
#
#         print(parChecker('((()))'))
#         print(parChecker('((()'))
# 注：栈是处理括号匹配极好的数据结构
# def check(strings):
#     s = Stack()
#     for string in strings:
#         if string == '(':
#             s.push(string)
#         elif string == '(':
#             try:
#                 s.pop()
#             except IndexError:
#                 return False
#             else:
#                 return False
#         return s.isEmpty()
#     print(check('((()))'))
#     print(check('()))'))
#符号匹配
#上面的两个程序仅用于'()'的匹配，实际上 Python 中常用的括号有 { } [ ] ( )。符号字符串如：{ { ( [ ] [ ] ) } ( ) } [ [ { { ( ( ) ) } } ] ] [ ] [ ] [ ] ( ) { }
# def check(strings):
#     s = Stack()
#     for string in strings:
#         if string in '{[(':
#             s.push(string)
#         elif string in ')]}':
#             try:
#                 match(open=s.pop(), close=string)
#             except(IndexError, ValueError):
#                 return False
#         else:
#             return False
#     return s.isEmpty()
# def match(open, close):
#     opens = '{[('
#     closers = '}])'
#     if opens.index(open) != closers.index(close):
#         raise ValueError
# print(check('[][][](){}'))
# print(check('[{()]'))
#queue队列模块详细介绍
#queue介绍:queue是python中的标准库，俗称队列。在python中，多个线程之间的数据是共享的，多个线程进行数据交换的时候，不能够保证数据的安全性和一致性，
# 所以当多个线程需要进行数据交换的时候，队列就出现了，队列可以完美解决线程间的数据交换，保证线程间数据的安全性和一致性。注意： 在python2.x中，模块名为Queue
#queue模块有三种队列及构造函数
#Python queue模块的FIFO队列先进先出。 queue.Queue(maxsize) #LIFO类似于堆，即先进后出。 queue.LifoQueue(maxsize) #还有一种是优先级队列级别越低越先出来。 queue.PriorityQueue(maxsize)
#queue模块中的常用方法
# import queue
# queue.qsize()返回队列的大小 queue.Empty()如果队列为空，返回True，反之False queue.full()如果队列满了，返回True，反之False
# queue.full与maxsize大小对应 queue.get([block[, timeout]])获取队列，立即取出一个元素， timeout超时时间
# queue.put(item[, timeout]]) 写入队列，立即放入一个元素， timeout超时时间 queue.get_nowait() 相当于queue.get(False) queue.put_nowait(item) 相当于queue.put(item, False)
#queue.join() 阻塞调用线程，直到队列中的所有任务被处理掉, 实际上意味着等到队列为空，再执行别的操作。queue.task_done() 在完成一项工作之后，queue.task_done()函数向任务已经完成的队列发送一个信号
# import queue
# q = queue.Queue()  #empty方法（如果队列为空，返回True）
# print(q.empty()) #输出：True
# full方法(如果队列满了，返回True)
# import queue
# q = queue.Queue(1)
# q.put('a')
# print(q.full()) #输出:True
#put方法和get方法
# import queue
# q = queue.Queue()
# q.put('a')
# q.put('b')
# print(q.get())
# #输出：a
# #qsize方法(返回队列里元素个数)
# import queue
# q = queue.Queue()
# q.put('a')
# q.put('b')
# print(q.qsize())
# #输出：2
# 字典
#字典是另一种可变容器模型，且可存储任意类型对象。字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1,key2 : value2,key3 : value3 } #注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。
#键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字。一个简单的字典实例：
# tinydict = {'name' : 'runoob' , 'like' : 123,'url': 'www.runoob.com'} #也可如此创造字典
# tinydict1 = { 'abc': 456 } tinydict2 = { 'abc': 123, 98.6: 37 }
#创建空字典：使用大括号 { } 创建空字典：
# # 使用大括号 {} 来创建空字典
# emptyDict = {'ddadsa':5545454,'okoklk':'iajjkk'}
# #打印字典
# print(emptyDict)
# #查看字典的数量
# print("length:",len(emptyDict))
# #查看类型
# print(type(emptyDict))
# #使用内建函数 dict() 创建字典：
# emptyDict = dict()
# #打印字典
# print(emptyDict)
# #查看字典的数量
# print("length:",len(emptyDict))
# #查看类型
# print(type(emptyDict))
#访问字典里的值
#把相应的键放入到括号中，如下实例：
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print ("tinydict['Name']: ", tinydict['Name'])
# print("tinydict['Age']:",tinydict['Age'])
#修改字典
#向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# tinydict['Age'] = 8  # 更新 Age
# tinydict['School'] = "菜鸟教程"  # 添加信息
# print ("tinydict['Age']: ", tinydict['Age'])
# print ("tinydict['School']: ", tinydict['School'])
#删除字典元素
#能删单一的元素也能清空字典，清空只需一项操作。显式删除一个字典用del命令，如下实例：
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# del tinydict['Name'] # 删除键 'Name'
# tinydict.clear()     # 清空字典
# del tinydict         # 删除字
# print ("tinydict['Age']: ", tinydict['Age'])
# print ("tinydict['School']: ", tinydict['School'])
#字典键的特性
#字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
#两个重要的点需要记住：1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print ("tinydict['Name']: ", tinydict['Name'])
#2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
# tinydict = {['Name']: 'Runoob', 'Age': 7}
# print ("tinydict['Name']: ", tinydict['Name'])
#字典内置函数&方法
#len(dict)：计算字典元素个数，即键的总数。 tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} len(tinydict)
#str(dict)：输出字典，可以打印的字符串表示。 tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} str(tinydict)
#type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。 tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} type(tinydict)
#Python字典包含了以下内置方法：dict.clear()删除字典内所有元素  dict.copy() 返回一个字典的浅复制 dict.fromkeys()创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# dict.get(key, default=None) 返回指定键的值，如果键不在字典中返回 default 设置的默认值 	key in dict 如果键在字典dict里返回true，否则返回false
# dict.items() 以列表返回一个视图对象 dict.keys() 返回一个视图对象 dict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
#dict.update(dict2) 把字典dict2的键/值对更新到dict里 dict.values() 返回一个视图对象 pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
#popitem() 返回并删除字典中的最后一对键和值。
#元组
#Python 的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号 ( )，列表使用方括号 [ ]。元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
#元组是有序且不可更改的集合。在 Python 中，元组是用圆括号编写的。
#创建元组：
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
#访问元组项目
#索引范围
#您可以通过指定范围的起点和终点来指定索引范围。指定范围后，返回值将是带有指定项目的新元组。
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])
#搜索将从索引 2（包括）开始，到索引 5（不包括）结束。请记住，第一项的索引为 0。
#负索引范围
#如果要从元组的末尾开始搜索，请指定负索引：
#此例将返回从索引 -4（包括）到索引 -1（排除）的项目：
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])
#更改元组值
#创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组。
#把元组转换为列表即可进行更改：
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1]='kiwi'
# x=tuple(y)
# print(x)
#遍历元组
#您可以使用 for 循环遍历元组项目。
#遍历项目并打印值：
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)
#添加项目
#元组一旦创建，您就无法向其添加项目。元组是不可改变的。
#创建有一个项目的元组
#如需创建仅包含一个项目的元组，您必须在该项目后添加一个逗号，否则 Python 无法将变量识别为元组。
# thistuple = ("apple",)
# print(type(thistuple))
#删除项目
#您无法删除元组中的项目。元组是不可更改的，因此您无法从中删除项目，但您可以完全删除元组：
# thistuple = ("apple", "banana", "cherry")
# del thistuple
#合并两个元组 如需连接两个或多个元组，您可以使用 + 运算符：
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)
#tuple() 构造函数
# 也可以使用 tuple() 构造函数来创建元组。
# thistuple = tuple(("apple", "banana", "cherry")) # 请注意双括号
# print(thistuple)
#元组方法 Python 提供两个可以在元组上使用的内建方法。
#count()  	返回元组中指定值出现的次数。 index()  在元组中搜索指定的值并返回它被找到的位置。
#二叉树顺序存储
# 链式存储
# class TreeNode:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.right = right
#         self.left = left
#
#
# class Bitree:
#     def __init__(self, root=None):
#         self.root = root
#
#     def preOrder(self, node):
#         if node is None:
#             return
#         print(node.data, end=" ")
#         self.preOrder(node.left)
#         self.preOrder(node.right)
#
#     def inOrder(self, node):
#         if node is None:
#             return
#         self.inOrder(node.left)
#         print(node.data, end=" ")
#         self.inOrder(node.right)
#
#     def postOrder(self, node):
#         if node is None:
#             return
#         self.postOrder(node.left)
#         self.postOrder(node.right)
#         print(node.data, end=" ")
#链表
# '''链表，注意正负坐标的转化，abs(posiIndex)+abs(negaIndex)=self.length\
#     另外需要注意到底是定位到index前一个元素，还是index元素本身'''
# import random
#
#
# class ChainCell():
#     '''本类是链表的基础元素类'''
#
#     def __init__(self, value=None, nextCell=None):
#         self.value = value;
#         self.next = nextCell;
#
#
# class Chain():
#     '''本类实现链表'''
#
#     def __init__(self, values=None):
#         '''初始化函数，如果有初始元素，要求以链表或者元组的形式传递'''
#         self.head = None
#         self.length = 0
#         if values:
#             for value in values:
#                 newCell = ChainCell(value)
#                 if not self.head:
#                     self.head = newCell
#                 else:
#                     self.last.next = newCell
#                 self.last = newCell
#                 self.length += 1
#
#     def isLegal(self, *args, **kargs):
#         '''该函数为类的内部函数，用来判断用户输入的下标是否合理。
#         如果下标不合理，则会报错，如果合理，则将index原路返回。
#         funcName为函数的名称，因为append函数比get等函数的边界大一'''
#
#         if not args:  # 判断index参数是以何种形式给出的，args和kargs里存储的都是实参，默认值不会出现在里面
#             if 'index' in kargs:
#                 index = kargs['index']
#             else:
#                 index = -1
#         else:
#             index = args[0]
#
#         if index > self.length - 1 or (index < 0 and abs(index) > self.length):
#             raise IndexError("index out of range")
#         elif not isinstance(index, int):
#             raise IndexError("下标必须是整数")
#         else:
#             return index
#
#     def checkLegal(func):
#         '''装饰器类，用来检查用户输入是否合法'''
#
#         def isLegalWarpFunc(self, *args, **kargs):  # 使用同一个装饰器是不是对被装饰的函数有统一的函数格式要求
#             self.isLegal(*args, **kargs)
#             return func(self, *args, **kargs)
#
#         return isLegalWarpFunc
#
#     def neg2pos(self, index):
#         if index < 0: index = self.length - abs(index)
#         return index
#
#     def getLast(self, index):
#         '''该函数用来获得index位置的上一个元素并返回'''
#         lastCell = self.head
#         for i in range(index - 1):
#             lastCell = lastCell.next
#         return lastCell
#
#     def append(self, index=-1, value=None):
#         '''向链表中的index位置之前添加元素'''
#         if not isinstance(index, int): raise IndexError('下标必须是整数')
#         if index < 0:
#             if abs(index) >= self.length:
#                 index = 0
#             else:
#                 index = self.length - abs(index)
#         if index >= self.length: index = -1
#
#         newCell = ChainCell(value)
#         if self.length == 0:
#             self.head = newCell
#         elif index == -1:  # 在最后插入元素
#             self.last.next, self.last = newCell, newCell
#         elif index == 0:  # 在第一个位置插入元素
#             newCell.next = self.head
#             self.head = newCell
#         else:
#             lastCell = self.getLast(index)
#             newCell.next = lastCell.next
#             lastCell.next = newCell
#         self.length += 1
#         return value
#
#     @checkLegal
#     def pop(self, index=-1):
#         '''弹出链表中的元素'''
#         # 没有办法直接删除最后一个元素，因为要修改上一个元素的next指针
#         index = self.neg2pos(index)
#         if index == 0:
#             if self.length > 1:
#                 self.head = self.head.next
#             else:
#                 self.head = None
#         else:
#             lastCell = self.getLast(index)
#             lastCell.next = lastCell.next.next
#         self.length -= 1
#
#     @checkLegal
#     def getCell(self, index):
#         '''对应“查”功能，是链表最基础的功能，时间复杂度为O(n)\
#         根据下标，获得某个链表元素的值,支持正负两种下标表示形式'''
#         index = self.neg2pos(index)
#         if index == 0:
#             return self.head.value
#         else:
#             lastCell = self.getLast(index)
#             return lastCell.next.value
#
#     @checkLegal
#     def setCell(self, index, value):
#         '''根据下标，设置某个链表元素的值'''
#         index = self.neg2pos(index)
#         lastCell = self.head
#         if index == 0:
#             lastCell.value = value
#             return value
#         lastCell = self.getLast(index)
#         lastCell.next.value = value
#         return value
#
#     def printChain(self):
#         '''输出所有的链表元素'''
#         # for i in range(self.length): 两种遍历方式
#         if not self.head:  # 或者if self.length==0
#             print('当前链表中没有元素！')
#             return
#         else:
#             lastCell = self.head
#             values = [lastCell.value]
#             while lastCell.next:
#                 lastCell = lastCell.next
#                 values.append(lastCell.value)
#             return values
#
#     def getLen(self):
#         '''输出链表的长度'''
#         # return self.length  最简单，适合维护了这个变量的情况
#         if not self.head:
#             return 0
#         else:
#             count = 1
#             lastCell = self.head
#             while lastCell.next:
#                 lastCell = lastCell.next
#                 count += 1
#             return count
#
#
# class listChain():
#     '''本类是用python的chain，实现类似于链表的功能，但是实际上底层结构和链表无关'''
#
#     def __init__(self, values=None):
#         self.values = [] if values == None else values
#
#     def append(self, index=-1, value=None):
#         '''Python insert函数，可以在指定的index前插入元素'''
#         self.values.insert(index, value)  # indet函数中，如果下标超出数据界限，则默认添加在数组两端
#
#     def pop(self, index=-1):
#         self.values.pop(index)
#
#     def getCell(self, index):
#         return self.values[index]
#
#     def setCell(self, index, value):
#         self.values[index] = value
#         return value
#
#     def printChain(self):
#         return self.values
#
#     def getLen(self):
#         return len(self.values)
#
#
# def testChain(c, index):
#     '''用于测试链表的功能，index 是随机产生的下标'''
#     commands = ['c.append({},{})'.format(index[0], index[1]),
#                 'c.pop(index={})'.format(index[2]),
#                 'z=c.getCell({})'.format(index[3]),
#                 'c.setCell(index={},value={})'.format(index[4], index[5])]
#     for line in commands:  # 通过循环，保证出现异常后，程序可以继续运行
#         try:
#             exec(line)
#         except Exception as e:
#             print(str(e))
#             continue
#
#
# # 用户初始化链表的列表，可以放到循环外边或者里面，因为浅拷贝的问题，会导致修改链表也修改li
# li = []
# for k in range(50):  # 设置测试多少次
#     print(li)
#     # li=[random.randint(-10,10) for i in range(random.randint(1,10))]
#     c1 = Chain(li)
#     c2 = listChain(li)
#     indexes = [random.randint(-10, 10) for i in range(6)]
#     testChain(c1, indexes)
#     testChain(c2, indexes)
#     if c1.printChain() != c2.printChain():
#         print("*" * 60)  # 字符串中的字符串，要注意区分单双引号
#         print(indexes)
#         print(li)

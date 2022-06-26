# -*- coding:utf-8 -*-
# 列表
# Python 集合（数组）
# Python 编程语言中有四种集合数据类型：
# 列表（List）是一种有序和可更改的集合。允许重复的成员。
# 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
# 集合（Set）是一个无序和无索引的集合。没有重复的成员。
# 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。
# 选择集合类型时，了解该类型的属性很有用。
# 为特定数据集选择正确的类型可能意味着保留含义，并且可能意味着提高效率或安全性。
# 创建列表：
# thislist = ["apple", "banana", "cherry"] #列表（List）是一种有序和可更改的集合。允许重复的成员
# print(thislist)
#访问项目 您可以通过引用索引号来访问列表项：
#打印列表的第二项：
# a = ["apple", "banana", "cherry"]
# print(a[1])
#负的索引
#负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目，依此类推。
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])
#索引范围
#您可以通过指定范围的起点和终点来指定索引范围。指定范围后，返回值将是包含指定项目的新列表。
#返回第三、第四、第五项：
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
#注释：搜索将从索引 2（包括）开始，到索引 5（不包括）结束。请记住，第一项的索引为 0。
#负索引的范围:如果要从列表末尾开始搜索，请指定负索引：
#此例将返回从索引 -4（包括）到索引 -1（排除）的项目：
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
#更改项目值:如需更改特定项目的值，请引用索引号：更改第二项：
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "mango"
# print(thislist)
#遍历列表:您可以使用 for 循环遍历列表项：
#逐个打印列表中的所有项目：
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)
#检查项目是否存在:如需确定列表中是否存在指定的项，请使用 in 关键字：
#检查列表中是否存在 “apple”：
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes")
#列表长度:如需确定列表中有多少项，请使用 len() 方法：
#打印列表中的项目数：
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))
#添加项目:如需将项目添加到列表的末尾，请使用 append() 方法：
#使用 append() 方法追加项目：
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
#要在指定的索引处添加项目，请使用 insert() 方法：
#插入项目作为第二个位置：
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1,"orange")
# print(thislist)
#删除项目:有几种方法可以从列表中删除项目：
#remove() 方法删除指定的项目：
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
#pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）：
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(0)
# print(thislist) #指定删除索引那个√
#del 关键字删除指定的索引：
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
#del 关键字也能完整地删除列表：
# thislist = ["apple", "banana", "cherry"]
# del thislist
#clear() 方法清空列表：
# thislist = ["apple", "banana", "cherry"]
# thislist.clear() #还剩[]
# print(thislist)
#复制列表:
# 您只能通过键入 list2 = list1 来复制列表，因为：list2 将只是对 list1 的引用，list1 中所做的更改也将自动在 list2 中进行。
#有一些方法可以进行复制，一种方法是使用内置的 List 方法 copy()。
#使用 copy() 方法来复制列表：
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)
#制作副本的另一种方法是使用内建的方法 list()。
#使用 list() 方法复制列表：
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)
#合并两个列表
#在 Python 中，有几种方法可以连接或串联两个或多个列表。最简单的方法之一是使用 + 运算符。
#合并两个列表：
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)
#连接两个列表的另一种方法是将 list2 中的所有项一个接一个地追加到 list1 中：
#把 list2 追加到 list1 中：
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
#     print(list1)
#或者，您可以使用 extend() 方法，其目的是将一个列表中的元素添加到另一列表中：
#使用 extend() 方法将 list2 添加到 list1 的末尾：
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)
#list() 构造函数
#也可以使用 list() 构造函数创建一个新列表。
#使用 list() 构造函数创建列表：
# thislist = list(("apple","banana","cherry"))# 请注意双括号
# print(thislist)
#列表方法
#Python 有一组可以在列表上使用的内建方法。
#count() 	返回具有指定值的元素数量。
#index() 	返回具有指定值的第一个元素的索引
#reverse() 	颠倒列表的顺序
#sort() 	对列表进行排序
# thislist = ["apple", "apple","banana", "cherry"]
# mylist =thislist.count("apple")
# print(mylist)
# thislist = ["apple", "apple","banana","cherry", "cherry"]
# mylist = thislist.index("cherry")
# print(mylist)
# thislist = ["apple", "apple","banana","cherry", "cherry"]
# thislist.reverse() # mylist = thislist.reverse() 该方法没有返回值
# print(thislist)
# thislist = ["apple", "apple","banana","cherry", "cherry"]
# thislist.reverse() #颠倒列表,反向排序
# thislist.sort() #对列表排序
# print(thislist)
# For 循环
#for 循环用于迭代序列（即列表，元组，字典，集合或字符串）。
#这与其他编程语言中的 for 关键字不太相似，而是更像其他面向对象编程语言中的迭代器方法。
#通过使用 for 循环，我们可以为列表、元组、集合中的每个项目等执行一组语句。
#打印 fruits 列表中的每种水果：
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#提示：for 循环不需要预先设置索引变量。
#循环遍历字符串
#甚至连字符串都是可迭代的对象，它们包含一系列的字符：
#循环遍历单词 "banana" 中的字母：
# for x in "banana":
#     print(x)
#break 语句
#通过使用 break 语句，我们可以在循环遍历所有项目之前停止循环：
#如果 x 是 "banana"，则退出循环：
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
#当 x 为 "banana" 时退出循环，但这次在打印之前中断：
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)
#continue 语句
#通过使用 continue 语句，我们可以停止循环的当前迭代，并继续下一个：
#不打印香蕉：
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)
#range() 函数
#如需循环一组代码指定的次数，我们可以使用 range() 函数，range() 函数返回一个数字序列，默认情况下从 0 开始，并递增 1（默认地），并以指定的数字结束。
#使用 range() 函数：
# for x in range(10):
#     print(x)
#注意：range(10) 不是 0 到 10 的值，而是值 0 到 9。
#range() 函数默认 0 为起始值，不过可以通过添加参数来指定起始值：range(3, 10)，这意味着值为 3 到 10（但不包括 10）：
#使用起始参数：
# for x in range(3, 10):
#     print(x)
#range() 函数默认将序列递增 1，但是可以通过添加第三个参数来指定增量值：range(2, 30, 3)：
#使用 3 递增序列（默认值为 1）：
# for x in range(3, 50, 6):
#     print(x)
#For 循环中的 Else
#for 循环中的 else 关键字指定循环结束时要执行的代码块：
#打印 0 到 9 的所有数字，并在循环结束时打印一条消息：
# for x in range(10):
#     print(x)
# eles:print("Finally finished!")
#嵌套循环
#嵌套循环是循环内的循环。“外循环”每迭代一次，“内循环”将执行一次：
#打印每个水果的每个形容词：
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,y)
#pass 语句
#for 语句不能为空，但是如果您处于某种原因写了无内容的 for 语句，请使用 pass 语句来避免错误。
# for x in [0, 1, 2]:
#     pass
#While 循环
#Python 有两个原始的循环命令：while 循环,for 循环
#while 循环
#如果使用 while 循环，只要条件为真，我们就可以执行一组语句。
#只要 i 小于 7，打印 i：
# i = 1
# while i < 7:
#     print(i)
#     i += 1
#注释：请记得递增 i，否则循环会永远继续。
#while 循环需要准备好相关的变量。在这个实例中，我们需要定义一个索引变量 i，我们将其设置为 1。
#break 语句
#如果使用 break 语句，即使 while 条件为真，我们也可以停止循环：
# i = 1
# while i < 7:
#     print(i)
#     if i == 3:
#         break
#     i += 1
#continue 语句
#如果使用 continue 语句，我们可以停止当前的迭代，并继续下一个：如果 i 等于 3，则继续下一个迭代：
# i = 0
# while i < 7:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
#else 语句
#通过使用 else 语句，当条件不再成立时，我们可以运行一次代码块：条件为假时打印一条消息：
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("dadafaff")
#函数
#函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
#定义一个函数
#你可以定义一个由自己想要功能的函数，以下是简单的规则：
#函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
#函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
#函数内容以冒号起始，并且缩进。
#return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
#语法
#Python 定义函数使用 def 关键字，一般格式如下
# def 函数名(参数列表):
#     函数体   默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
#让我们使用函数来输出"Hello World！"：
# def hello():
#     print("hello")
# hello()
#更复杂点的应用，函数中带上参数变量:
# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a = 4
# b = 5
# print(max(a,b))
#计算面积函数:
# def area(width,height):
#     return width * height
# def print_welcome(name):
#     print("Welcome",name)
# print_welcome("Runoob")
# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))
#函数调用
#定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。
#如下实例调用了 printme() 函数：
# def printme(str):
#     #打印任何传入的字符串
#     print(str)
#     return
# #调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")
#参数传递
#在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：
# a = [1,2,3]
# a = "Runoob"
#以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），
# 可以是指向 List 类型对象，也可以是指向 String 类型对象。
#可更改(mutable)与不可更改(immutable)对象
#在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
#不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
#可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。python 函数的参数传递：
#不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
#可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
#python 传不可变对象实例
#通过 id() 函数来查看内存地址变化：
# def chang(a):
#     print(id(a)) # 指向的是同一个对象
#     a = 10
#     print(id(a)) # 一个新对象
#     return
# a = 1
# print(id(a))
# chang(a)
#可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。
#传可变对象实例
#可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1,2,3,4])
#     print("函数内取值:",mylist)
#     return
# # 调用changeme函数
# mylist = [10,20,30]
# changeme(mylist)
# print("函数外取值:", mylist)
#传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下：
#参数
#以下是调用函数时可使用的正式参数类型：必需参数 关键字参数 默认参数 不定长参数
#必需参数
#必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：
#可写函数说明
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
# # 调用 printme 函数，不加参数会报错
# printme()
#关键字参数
#关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
#以下实例在函数 printme() 调用时使用参数名：
#可写函数说明
# def printme( str ):
#     "打印任何传入的字符串"
#     print(str)
#     return
# #调用printme函数
# printme( str = "菜鸟教程")
#以下实例中演示了函数参数的使用不需要使用指定顺序：
#可写函数说明
# def printinfo( name, age ):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# printinfo( age=50,name="runoob")
#默认参数
#调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
#可写函数说明
# def printinfo( name, age = 35 ):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# #调用printinfo函数
# printinfo(age=50,name="runoob")
# print("----------------------")
# printinfo(name="runoob")
#不定长参数
#你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
# def printinfo(arg1,*vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
# # 调用printinfo 函数
# printinfo( 70, 60, 50,50 )
#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
# 可写函数说明
# def printinfo( arg1, *vartuple ):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#         return
# printinfo(10)
# printinfo(70,60,50)
#还有一种就是参数带两个星号 **基本语法如下：
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
#加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
# def printinfo( arg1, **vardict ):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
# printinfo(1,a=2,b=3)
#声明函数时，参数中星号 * 可以单独出现，例如:
# def f(a,b,*,c):
#     return a + b + c
#如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
# def f(a,b,*,c):
#     return a + b + c
# f(1,2,c=3)
#匿名函数
#Python 使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
#lambda 只是一个表达式，函数体比 def 简单很多。
#lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
#lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
#虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#语法
#lambda 函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
#设置参数 a 加上 10:
# x = lambda a:a+10
# print(x(5))
#以下实例匿名函数设置两个参数：
# 可写函数说明
# sum = lambda arg1,arg2:arg1+arg2
# # 调用sum函数
# print ("相加后的值为 : ", sum( 10, 20 ))
# print ("相加后的值为 : ", sum( 20, 20 ))
#我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
# #以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
# def myfunc(n):
#     return lambda a:a*n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))
#return 语句
#return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：
# 可写函数说明
# def sum( arg1, arg2 ):
#    # 返回2个参数的和."
#    total = arg1 + arg2
#    print("函数内 : ", total)
#    return total
# # 调用sum函数
# total = sum( 10, 20 )
# print ("函数外 : ", total)
#强制位置参数
#Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
# f(10,20,c=30,d=40, e=50, f=60)
#导入模块的3种方式
#day2.py
# def say():
#     print("Hello,World!")
# say.py
# hello.say() #显然，hello.py 文件和 say.py 文件并不在同一目录,Python 解释器抛出了 ModuleNotFoundError 异常
#导入模块方式一：临时添加模块完整路径
#模块文件的存储位置，可以临时添加到 sys.path 变量中，即向 sys.path 中添加 D:\python_module（hello.py 所在目录），在 say.py 中的开头位置添加如下代码：
# import day2
# import sys
# sys.path.append('C:\\Users\Yuzhongxiang\PycharmProjects\ceshi')
# day2.say()
# print(sys.path)
#注意：在添加完整路径中，路径中的 '\' 需要使用 \ 进行转义，否则会导致语法错误。再次运行 say.py 文件，运行结果如下：Hello,World!
#可以看到，程序成功运行。在此基础上，我们在 say.py 文件中输出 sys.path 变量的值，会得到以下结果： ['C:\\Users\\Yuzhongxiang\\Desktop', 'C:\\Users\\Yuzhongxiang\\PycharmProjects\\ceshi', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\python38.zip', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\DLLs', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\lib', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38', 'C:\\Users\\Yuzhongxiang\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\lib\\site-packages', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\lib\\site-packages\\win32', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\lib\\site-packages\\win32\\lib', 'C:\\Users\\Yuzhongxiang\\.conda\\envs\\py38\\lib\\site-packages\\Pythonwin', 'C:\\Users\\Yuzhongxiang\\PycharmProjects\\ceshi']
# 该输出信息中，红色部分就是临时添加进去的存储路径。需要注意的是，通过该方法添加的目录，只能在执行当前文件的窗口中有效，窗口关闭后即失效。
#导入模块方式二：将模块保存到指定位置
#如果要安装某些通用性模块，比如复数功能支持的模块、矩阵计算支持的模块、图形界面支持的模块等，这些都属于对 Python 本身进行扩展的模块，这种模块应该直接安装在 Python 内部，以便被所有程序共享，此时就可借助于 Python 默认的模块加载路径。
#Python 程序默认的模块加载路径保存在 sys.path 变量中，因此，我们可以在 say.py 程序文件中先看看 sys.path 中保存的默认加载路径，向 say.py 文件中输出 sys.path 的值，如下所示：
#上面的运行结果中，列出的所有路径都是 Python 默认的模块加载路径，但通常来说，我们默认将 Python 的扩展模块添加在 lib\site-packages 路径下，它专门用于存放 Python 的扩展模块和包。
#导入模块方式三：设置环境变量
#PYTHONPATH 环境变量（简称 path 变量）的值是很多路径组成的集合，Python 解释器会按照 path 包含的路径进行一次搜索，直到找到指定要加载的模块。当然，如果最终依旧没有找到，则 Python 就报 ModuleNotFoundError 异常。
# 第一条路径为一个点（.），表示当前路径，当运行 Python 程序时，Python 将可以从当前路径加载模块；
# 第二条路径为 d:\python_ module，当运行 Python 程序时，Python 将可以从 d:\python_ module 中加载模块。
#然后点击“确定”，即成功设置 path 环境变量。此时，我们只需要将模块文件移动到和引入该模块的文件相同的目录，或者移动到 d:\python_ module 路径下，该模块就能被成功加载。

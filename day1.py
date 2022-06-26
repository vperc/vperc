# # print(*objects,sep='',end='\n',file=foo.txt,flush=False)
# print(1)
# print("hello world")
# a = 1
# b = 'runoob'
# print(a,b)
# print("aaa""bbb")
# print("aaa","bbb")
# print("www","baidu","com",sep=".")#设置间隔符
# import time
#
# print("---RUNOOB EXAMOLE :  Loading 效果---")
# print("Loading",end = "")
# for i in range(20):
#     print(".",end='',flush=True)
#     time.sleep(0.5)
#输出字符串和数字
# print("runoob")
# print(100)
# str = 'runoob'
# print(str)
# L = [1,2,'a']
# print(L)
# t = (1,2,'a')
# print(t)
# d = {'a':1,'b':2}
# print(d)
# 参数格式化
# # str = "the length of (%s) is %d" %('runoob',len('runoob'))
# # print(str)
# str = "the length of {} is {}".format('runoob',len('runoob'))
# print(str)
#python字符串格式化符号
# %c 格式化字符及其ASCII码 , %s格式化字符串 ,%d格式化整数,%u 格式化无符号整型 %o 格式化无符号八进制数 %x 格式化无符号十六进制数 %X格式化无符号十六进制数（大写）
# %f 格式化浮点数字,可指定小数后的精度 %e 用科学计数法格式化浮点数 %E 作用同%e,用科学计数法格式化浮点数 %g %f 和 %E 的简写 %p 用十六进制数格式化变量的地址
# str = "the length of (%f) is %d" %(555.545000878489454,len('runoob'))
# print(str)
#格式化操作符辅助指令
# *定义宽度和小数点精度 -用做左对齐 +在正数前面显示加号（+）<sp>在正数前面显示空格 在八进制数前面零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0显示的数字前面填充'0'而不是默认的空格 %'%%'输出一个单一的'%' (var)映射变量(字典参数) m.n.m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
#格式化输出16进制,十进制,八进制整数
# %x--hex十六进制
# %d--dec十六进制
# %o---oct八进制
# nHex = 0xFF
# print("nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex))
#格式化输出浮点数(float)
pi = 3.141592653
# print('%10.3f'%pi)#字段宽10,精度3
# print("pi = %*.*f" %(10,3,pi))#用*从后面的元组中读取字段宽度或精度
# print('%010.3f' % pi) #用0填充空白
# print('%-10.3f' %pi) #左对齐
# print('%+f' %pi ) #显示正负号
#自动换行
# for i in range(0,6):
#     print(i,end="  ")
# # #print不换行
# # for i in range(0,3):
# #     print(i,end='')
#创建变量
# x = 10
# y = "Bill"
# print(x)
# print(y)
# x = 5
# x = "Steve"
# print(x)
#字符串变量可以使用单引号或双引号进行声明：
# x = "Bill"
# x = 'Bill'
# _car_name = "lost" #  变量名称区分大小写Age,age,AGE为三个不同的变量
#向多个变量赋值
# x,y,z="Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# 您可以在一行中为多个变量分配相同的值：
# x=y=z="daqba"
# print(x)
# print(y)
# print(z)
# 输出变量
# x = "aweone"
# print("sadd" + x )
# 您还可以使用 + 字符将变量与另一个变量相加：
# x = "Python is "
# y = "awesome"
# z =  x + y
# print(z)
# 对于数字，+ 字符用作数学运算符：
# x = 5
# y = 10
# print(x + y)
#如果您尝试组合字符串和数字，Python 会给出错误：
# x = 10
# y = "Bill"
# print(x + y)
#全局变量
# 在函数外部创建的变量（如上述所有实例所示）称为全局变量。
# # 全局变量可以被函数内部和外部的每个人使用。
# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()
#如果在函数内部创建具有相同名称的变量，则该变量将是局部变量，并且只能在函数内部使用。具有相同名称的全局变量将保留原样，并拥有原始值。
#在函数内部创建一个与全局变量同名的变量：
# x = "awesome"
# def myfunc():
#     x = "dadkakdkd"
#     print("daaaddad" + x)
# myfunc()
# print("adxxx" + x)
#global 关键字
#通常，在函数内部创建变量时，该变量是局部变量，只能在该函数内部使用。
#要在函数内部创建全局变量，您可以使用 global 关键字。
# def jbk():
#     global x   #global关键字全局变量
#     x = "dadad"
# jbk()
# print("rafa" + x)
# 另外，如果要在函数内部更改全局变量，请使用 global 关键字。
# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)
#输出格式美化
#Python两种输出值的方式: 表达式语句和 print() 函数。
#第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 foo.txt 引用。如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
#如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
# s = 'Hello, Runoob'
# # # print(str(s))
# # # print(repr(s))
# # print(str(1/7))
# x = 10 * 3.25
# y = 200 * 200
# # s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
# # print(s)
# #  repr() 函数可以转义字符串中的特殊字符
# # hello = 'hellow,runoob\n'
# # hellos = repr(hello)
# # print(hellos)
# # repr() 的参数可以是 Python 的任何对象
# print(repr((x,y,('Google','Runoob'))))
# for x in range(1, 11):
#    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#      # 注意前一行 'end' 的使用
#    print(repr(x*x*x).rjust(4))
# for x in range(1,11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
#注意：在第一个例子中, 每列间的空格由 print() 添加。这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
#还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))
#str.format() 的基本使用如下:
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
#在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
# print('{1} 和 {0}'.format('Google', 'Runoob'))
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
#位置及关键字参数可以任意的结合:
# >>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# 站点列表 Google, Runoob, 和 Taobao。
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
# import math
# print('常量的PI近似值为：{}。'.format(math.pi))
# print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
# import math
# print('常量 PI 的值近似为 {:0.3f}。'.format(math.pi))
# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name,number in table.items():
#     print('{0:10}==>{1:10d}'.format(name,number))
#  如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# #也可以通过在 table 变量前使用 ** 来实现相同的功能：
# # table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# # print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# #旧式字符串格式化
# # import math
# # print('常量 PI 的值近似为：%5.3f。' % math.pi)
# #读取键盘输入
# #Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
# # str = input("请输入：");
# # print ("你输入的内容是: ", str)
# #读和写文件
# #open() 将会返回一个 file 对象，基本语法格式如下:
# #filename：包含了你要访问的文件名称的字符串值。mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# # open(filename, mode)
# #以下实例将字符串写入到文件 foo.txt 中：
# #打开一个文件
# f = open("foo.txt","w")
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# #关闭打开的文件
# f.close()
# #第一个参数为要打开的文件名。
# #第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容;
# # 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。
# #文件对象的方法
# #本节中剩下的例子假设已经创建了一个称为 f 的文件对象。
# #f.read()
# # # 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# # size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。以下实例假定文件 foo.txt 已存在（上面实例中已创建）
# f = open("foo.txt", "r")
# str = f.read()
# print(str)
# f.close()
#f.readline()
#f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# # 打开一个文件
# f = open("foo.txt", "r")
# str = f.readline()
# print(str)
# # 关闭打开的文件
# f.close()
#f.readlines()
# f.readlines() 将返回该文件中包含的所有行。 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
# f = open("foo.txt", "r")
# str = f.readlines()
# print(str)
# f.close()
#另一种方式是迭代一个文件对象然后读取每行:
# f = open("foo.txt", "r")
# for line in f:
#     print(line,end="")
# f.close() #这个方法很简单, 但是并没有提供一个很好的控制。
#f.write()
#f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# f = open("foo.txt", "w")
# num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# print(num)
# f.close()
#如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# 打开一个文件
# f = open("foo1.txt", "w")
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
# print(s)
# # 关闭打开的文件
# f.close()
#f.tell()
#f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
#f.seek()
#如果要改变文件指针当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符。seek(x,1) ： 表示从当前位置往后移动x个字符。 seek(-x,2)：表示从文件的结尾往前移动x个字符
#from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
# f = open("foo.txt", 'rb+')
# f.write(b'0123456789abcdef')
# f.seek(5)# 移动到文件的第六个字节
# f.read(1)
# f.seek(-3, 2)# 移动到文件的倒数第三字节
# f.read(1)
#f.close()
# 在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
# 文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
# f.close()
# f.read()
# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
# with open('foo.txt', 'r') as f:
#      read_data = f.read()
# f.close() #文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。
#Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
# Python 编程中 if 语句用于控制程序的执行，基本形式为：
# if 判断条件：
#     执行语句……
# else：
#     执行语句……
#其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。
# else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句。
# flag = False
# name = 'luren'
# if name == 'python':# 判断变量是否为 python
#     flag = True# 条件成立时设置标志为真
#     print("fafafaf") # 并输出欢迎信息
# else:
#     print(name) # 条件不成立时输出变量名称
#if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。当判断条件为多个值时，可以使用以下形式：
# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……
# num = 5
# if num == 3:            # 判断num的值
#     print('boss')
# elif num == 2:
#     print('user')
# elif num == 1:
#     print('worker')
# elif num < 0:           # 值小于零时输出
#     print('error')
# else:
#     print('roadman')    # 条件均不成立时输出
#由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
# 可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
# 例3：if语句多个条件
# num = 9
# if num >= 0 and num <= 10:    # 判断值是否在0~10之间
#     print('hello')
# num = 10
# if num < 0 or num > 10:    # 判断值是否在小于0或大于10
#     print('hello')
# else:
#     print('undefine') # 输出结果: undefine
# num = 8
# # 判断值是否在0~5或者10~15之间
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
#     print('hello')
# else:
#     print('undefine')
# # 输出结果: undefine
#当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，
# 此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，即大于和小于在没有括号的情况下会比与或要优先判断。
#简单的语句组
#你也可以在同一行的位置上使用if条件判断语句，如下实例：
# var = 100
# if ( var  == 100 ) :print ("变量 var 的值为100")
# else:print ("Good bye!")




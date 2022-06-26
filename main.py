importlib.import_module()
# a=1 #这是一个数字
# print(a)
# c="打卡的垃圾的骄傲"#这是一个字符串
# print(c)
# f = [1,2,3,4,5,6]#这是一个列表
# print(f)
# g = (8,9,10) #这是一个元祖
# print(g)
# p = {1,2,3} #这是一个集合
# print(p)
# l = {"a":1,"b":2}
# print(l)
# print(type(l))#这是一个字典
#
# age = 18
# print("我今年%d岁了"%age)
# name = "小老表"
# print("我是大老表,我还有一个弟弟叫%s"%name)
# f1 = 3.14
# print("圆周率等于%.3f"%f1)
# print("我的名字是%s,我的年龄是%d,我知道圆周率是%.3f"%(name,age,f1))
#
# age2 = 22
# name = '张三'
# print("我的名字是{},\n今年{}岁了".format(name,age2))
#
# print("===========我的名片============")
# name = 'yuzx'
# qq = '2861943172'
# phone = '17695814045'
# address = '成都市'
# print("姓名:{}\nQQ:{}\n手机:{}\n地址:{}".format(name,qq,phone,address))
# print("=============================")
#
# p = input("请输入你的银行卡密码:")
# print(type(p))
# print("你的银行卡密码是{}".format(p)) # 6666666------> "6666666"
# #input函数可以获取用户输入的内容,但是内容统一做字符串处理
# w = int(p)
# print(type(w))
#
# a = 10
# b = 20
# print(a+b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# p = input("请输入你要的价格:")
# w = eval(p)
# print(w)
# print(type(w))
#去上网吧，需判断年龄，如果大于18岁就可以进入，如果小于18岁，回家写作业

# age = 19
# if age<=18:
#     print("回家写作业")
#     print(1)
#     print(1)
#     print(1)
#     print(1)
# else: # 表示其他情况 也就是说其他年龄超过18岁
#     print("欢迎光临")
# num1 = 10
# num2 = 20
# print(num1==num2)
# print(num1!=num2)
# print(num1>=num2)
# if(1!=1) or (10>3):
#     print("条件成立")

#进入火车站，有票就进入，没票就回家

# piao = True  # 1 代表True
# if piao == True:
#     print("有票，里面请")
# else:
#     print("没票,回家去吧")

# name = input("name:")
# age = input("age:")
# hometown = input("hometown:")
# hobbie = input("hobbie:")
# msg =f'''
# --------------------info of {name}--------------------
# Name :{name}
# Age :{age}
# job :{hometown}
# Hobbie :{hobbie}
# --------------------- end ----------------------
# '''
# print(msg)

# #3.3.2.1. 自定义模块属性访问
# import sys
# from types import ModuleType
#
# class VerboseModule(ModuleType):
#     def __repr__(self):
#         return f'Verbose {self.__name__}'
#
#     def __setattr__(self, attr, value):
#         print(f'Setting {attr}...')
#         super().__setattr__(attr, value)
#
# sys.modules[__name__].__class__ = VerboseModule

#5.2.1. 常规包
#常规包通常以一个包含 __init__.py 文件的目录形式实现。
# 当一个常规包被导入时，这个 __init__.py 文件会隐式地被执行，它所定义的对象会被绑定到该包命名空间中的名称。
# __init__.py 文件可以包含与任何其他模块中所包含的 Python 代码相似的代码，Python 将在模块被导入时为其添加额外的属性。

#python标准库:内置函数
def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True
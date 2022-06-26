#6. 模块
#Python有一种方法可以把定义放在一个文件里，并在脚本或解释器的交互式实例中使用它们。
#这样的文件被称作模块 ；模块中的定义可以导入到其它模块或者主模块（你在顶级和计算器模式下执行的脚本中可以访问的变量集合)。
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

import fibo
print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib
print(fib(500))


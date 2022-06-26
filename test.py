#Python 的 for 语句与 C 或 Pascal 中的不同。Python 的 for 语句不迭代算术递增数值（如 Pascal）
# 或是给予用户定义迭代步骤和暂停条件的能力（如 C），而是迭代列表或字符串等任意序列，元素的迭代顺序与在序列中出现的顺序一致。
words = ['cat','window','defenestrate']
for w in words:
    print(w,len(w))
#遍历集合时修改集合的内容，会很容易生成错误的结果。因此不能直接进行循环，而是应遍历该集合的副本或创建新的集合：
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

#range函数遍历数字序列
print("range遍历数字序列")
for i in range(10):
    print(i)
list(range(5, 10))
list(range(0, 10, 3))
list(range(-10, -100, -30))

print("按索引迭代序列")
a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i,a[i])
for i,v in enumerate(a):
    print(i,v)

#在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

#continue 语句也借鉴自 C 语言，表示继续执行循环的下一次迭代
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
 #pass 语句不执行任何操作。语法上需要一个语句，但程序不实际执行任何动作时，可以使用该语句
    # while True:
    #     pass

#python3.10 match语句

#定义函数

#参数默认值

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


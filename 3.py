import random
import string

count = 0
while count < 3:
    car_nums = []#存储用户选择的车号
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase) #生成车牌的第一个字母
        n2 = "".join(random.sample(string.ascii_uppercase+string.digits,5))
        c_num = f"京{n1}-{n2}"
        car_nums.append(c_num) #把生成的号添加到列表
        print(i+1,c_num)
        choice = input("输入你喜欢的号").strip()
        if choice in car_nums: #代表用户选择是合法的
            print(f"恭喜你选择了新车牌号:{choice}")
            exit("Good luck.")
        else:
            print("不合法的选择.....")
        count += 1
# random.choice('abcdefghijk')
# s = 'abcdefghijklm'
# random.sample(s,3)
# random.randint(1,100)

import random
money = 100
num = random.randint(0, 10)

while money > 0:
    a = input("请输入一个数字：")
    a = int(a)
    if a > num:
        print("输入的数字过大")
        money -= 10
    elif a < num:
        print("输入的数字过小")
        money -= 10
    else:
        print("输入正确。")
        break

print("余额为：", money)

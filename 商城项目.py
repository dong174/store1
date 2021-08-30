'''
    1.用金钱
    2.空的购物车
    3.有足够商品
    4.正常购物
        是否有这个商品
        金钱是否足够
            添加购物车

    技术选型：
        1.判断
        2.循环
        3.容器技术
        4.输入input
        5.打印
    任务1：
        10张联想优惠券，0.5
        20张老干妈优惠券：0.6
        10张乌江榨菜优惠券，0.9
    最后使用优惠券来结算
'''
# 1.准备一个商品柜  准备优惠券
import time

shop = [
    ["联想电脑", 4500],
    ["Mac Pc", 12000],
    ["HUA WEI WATCH", 1200],
    ["海尔洗衣机", 5000],
    ["卫龙辣条", 3.5],
    ["老干妈", 15],
    ["乌江榨菜", 1.5]
]

from random import choice
discount = []
discount_lenovo = ['联想电脑5折券']
discount_old = ['老干妈六折券']
discount_wuzha = ['乌江榨菜九折券']
for i in range(10):
    discount.extend(discount_lenovo)
for i in range(20):
    discount.extend(discount_old)
for i in range(10):
    discount.extend(discount_wuzha)
# print(discount)
choose = choice(discount)
print("您的优惠券为：", choose)
# 2.准备钱包
while True:
    money = input("请初始化您的余额：")
    if money.isdigit():
        money = int(money)
        break
    else:
        print("--------请输入数字！！！--------")

# 3.空购物车
mycart = []

# 4.正常买东西

while True:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    # 买东西
    chose = input("亲输入您要的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        #  这个商品是否存在
        if chose >= len(shop):  # len(shop) = 7
            print("该商品不存在！别瞎弄！请重新输入：")
        else:
            # 看钱够不够
            if money < shop[chose][1]:
                print("对不起，您的余额不足，穷鬼，请到其他地方购买！")
            elif choose in discount_lenovo and chose == 0:
                mycart.append(shop[chose])
                money = money - shop[chose][1] * 0.5
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
            elif choose in discount_old and chose == 5:
                mycart.append(shop[chose])
                money = money - shop[chose][1] * 0.6
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
            elif choose in discount_wuzha and chose == 6:
                mycart.append(shop[chose])
                money = money - shop[chose][1] * 0.9
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
            else:
                mycart.append(shop[chose])
                money = money - shop[chose][1]
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法！别瞎弄！请重新输入：")

# 结算,打印购物小条
print("以下是您的购物小条，请查收：")
print("----------------------------")
for key, value in enumerate(mycart):
    print(key, value)
print("您本次余额还剩：￥", money)
print("----------------------------")  #

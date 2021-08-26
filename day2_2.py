# a1 = int(input("请输入一个数字："))
# a2 = int(input("请输入一个数字："))
# a3 = int(input("请输入一个数字："))
# a4 = int(input("请输入一个数字："))
# a5 = int(input("请输入一个数字："))
# a6 = int(input("请输入一个数字："))
# a7 = int(input("请输入一个数字："))
# a8 = int(input("请输入一个数字："))
# a9 = int(input("请输入一个数字："))
# a10 = int(input("请输入一个数字："))
# sum=(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)
# print("十个数的和为：",sum)
# print("平均数为",sum/10)
# print("最大值为：",max(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10))


# import random
#
# a=random.randint(50,150)
# print(a)

#判断三角形
# a=input("第一条边")
# b=input("第二条边")
# c=input("第三条边")
# a,b,c=int(a),int(b),int(c)
# if a+b>c and a+c>b and b+c>a:
#     print("可形成三角形")
#     if a==b or b==c or a==c:
#         print("等腰三角形")
#         if a == b and a == c and b == c:
#             print("等边三角形")
#     elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         print("直角三角形")
# else:
#     print("不能形成三角形")

#调换
# A = 56
# B = 78
# C = B - A
# A = A + C
# B = B - C
# print(A,B)

#登录账号
# a=0
# while a<3:
#     name=input("请输入用户名")
#     pwd=input('请输入密码')
#     if pwd=='admin' and name=="root":
#         print('密码正确。')
#         break
#     else:
#         print('密码错误。')
#     a+=1
# else:
#     print("三次密码均输入错误。")

#三角图形
# for i in range(5):
#     # print(i)
#     print(" "*(5-i),end="")
#     print("* "*(i+1))

#正9
# for i in range(1, 10):  #行数
#     for j in range(1, i+1):
#         print(j,'*', i,'=',j*i,end='\t')
#     print()

#倒9
# for i in range(-9, 0):  #行数
#     for j in range(1, -i+1):
#         print(j,'*', -i,'=',j*(-i),end='\t')
#     print()

#青蛙爬井
# meter=0
# day=0
# while meter<20:
#     meter+=3
#     day+=1
#     if meter>20:
#         break
#     else:
#         meter-=2
# print(day)


#阶乘和
# i=0
# s=0
# t=1
# for i in range(1,21):
#     t*=i
#     s+=t
# print(s)
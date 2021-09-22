
# class Air:
#     __brand = ''
#     __price = 0
#     __time = 0
#
#     def setBrand(self, brand):
#         self.__brand = brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def setPrice(self, price):
#         if price <= 0:
#             print('价格不能为零为负！')
#         else:
#             self.__price = int(price)
#
#     def getPrice(self):
#         return self.__price
#
#     def setTime(self, time):
#         if time < 0:
#             print('时间不能为负！！')
#         else:
#             self.__time = int(time)
#
#     def power_on(self):
#         print('空调开机了...')
#
#     def shut_down(self):
#         print('空调将在', self.__time, '分钟后自动关闭...')
#
#     def show(self):
#         print('空调品牌是', self.__brand, '空调价格为', self.__price, '元！')
#
#
# p = Air()
# p.power_on()
# p.setBrand(input('输入空调品牌：'))
# p.setPrice(int(input('输入空调价格：')))
# p.show()
# p.setTime(int(input('空调在多少分钟后关机：')))
# p.shut_down()

# class Student:
#     __username = None
#     __age =  None
#
#     def setUsername(self,username):
#         self.__username =  username
#
#     def getUsername(self):
#         return self.__username
#
#     def setAge(self,age):
#         if age > 120 or age < 0:
#             print("您年龄输入非法！")
#         else:
#             self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def showMe(self):
#         print("大家好，我叫",self.__username,"，今年",self.__age,"岁了！")
#
#     def compare(self,student):# self代表我自己    student代表另一个人
#         if self.__age > student.getAge():
#             print("我比同桌大",(self.__age - student.getAge()),"岁！")
#         elif self.__age < student.getAge():
#             print("我比同桌小", ( student.getAge()- self.__age),"岁！")
#         else:
#             print("我俩一样大！")
#
# s = Student()
# s.setUsername("旺财")
# s.setAge(55)
#
# s1 = Student()
# s1.setUsername("李四")
# s1.setAge(56)
#
# s.compare(s1) # 旺财要和李四比较
# s1.compare(s)

# class People:
#     __name = ''
#     __gender = ''
#     __age = 0
#     __cost = 0   # 剩余话费
#     __brand = ''   # 品牌
#     __battery = 0  # 电池容量
#     __size = 0    # 屏幕大小
#     __standby = 0   # 最大待机时长
#     __integral = 0  # 积分
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setGender(self, gender):
#         self.__gender = gender
#
#     def getGender(self):
#         return self.__gender
#
#     def setAge(self, age):
#         if age <= 0 or age >= 120:
#             print('年龄非法！')
#         else:
#             self.__age = int(age)
#
#     def getAge(self):
#         return self.__age
#
#     def setCost(self, cost):
#         self.__cost = float(cost)
#
#     def getCost(self):
#         return self.__cost
#
#     def setBrand(self, brand):
#         self.__brand = brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def setBattery(self, battery):
#         if battery < 0:
#             print('电池容量不能为负！')
#         else:
#             self.__battery = float(battery)
#
#     def getBattery(self):
#         return self.__battery
#
#     def setSize(self, size):
#         if size <= 0:
#             print('屏幕大小输入非法！')
#         else:
#             self.__size = int(size)
#
#     def getSize(self):
#         return self.__size
#
#     def setStandby(self,standby):
#         self.__standby = int(standby)
#
#     def getStandby(self):
#         return self.__standby
#
#     def setIntegral(self, integral):
#         if integral < 0:
#             print('积分不能为负！')
#         else:
#             self.__integral = int(integral)
#
#     def getIntegral(self):
#         return self.__integral
#
#     def show(self):
#         print('姓名', self.__name, '\n性别', self.__gender, '\n年龄', self.__age,'\n所拥有的手机剩余话费',
#               self.__cost, '元！\n手机品牌', self.__brand,'\n手机电池容量', self.__battery, '%\n屏幕大小',
#               self.__size, '寸\n最大待机时长',self.__standby, '分钟\n所拥有积分：', self.__integral)
#
#
# p = People()
# p.setName(input('输入姓名'))
# p.setGender(input('输入性别'))
# p.setAge(int(input('输入年龄')))
# p.setCost(float(input('输入手机剩余话费')))
# p.setBrand(input('输入手机品牌'))
# p.setBattery(float(input('输入电池容量')))
# p.setSize(int(input('输入手机屏幕大小')))
# p.setStandby(int(input('输入手机最大待机时长')))
# p.setIntegral(int(input('输入拥有积分')))
# p.show()
# cc = p.getCost()
# dd = p.getIntegral()
#
# while True:
#     a = int(input('需要打电话还是发短信：（1或2）'))
#     if a == 1:
#         a_1 = input('输入短信内容：')
#         print('短信内容为：\n', a_1)
#     elif a == 2:
#         a_1 = int(input('输入电话号码：'))
#         a_2 = int(input('输入打多长时间：'))
#         if a_1 == None: print('不能为空！')
#         elif a_1 <= 1: print('电话费不够了！')
#         else:
#             print('电话已拨通！')
#         if a_2 >= 0 and a_2 <= 10:
#             if dd >= a_2 * 15:
#                 dd -= a_2 * 15
#             else:
#                 cc -= a_2 * 1
#         elif a_2 > 10 and a_2 <=20:
#             if dd >= a_2 * 39:
#                 dd -= a_2 * 39
#             else:
#                 cc -= a_2 * 0.8
#         else:
#             if dd >= a_2 * 48:
#                 dd -= a_2 * 48
#             else:
#                 cc -= a_2 * 0.65
#
#         print('剩余话费为：', cc)
#         print('剩余积分为：', dd)

# class student():
#     __name = ''
#     __age = 0
#     __sex = ''
#     __height = 0
#     __weight = 0
#     __grade = 0
#     __address = ''
#     __phone = 0
#
#     def learn(self,time):
#         print("学习了",time,"小时")
#     def play(self,game_name):
#         print("玩的是",game_name)
#     def program(self,row):
#         print("敲了",row,"行代码")
#     def sum(self,a,b):
#         print("和为：",a+b)
# s = student()
# s.learn(20)
# s.play("植物大战僵尸")
# s.program(8888)
# s.sum(1,5)


# class car():
#     __model = ""
#     __num = 0
#     __color = ''
#     __weight = 0
#     __size = 0
#     def setModel(self,model):
#         self.__model = model
#     def run(self,function):
#         print("此车为",self.__model,"擅长",function)
# c=car()
# c.setModel("法拉利")
# c.run("贵")
# c.setModel("宝马")
# c.run("贵")
# c.setModel("铃木")
# c.run("跑")
# c.setModel("五菱")
# c.run("神驹")
# c.setModel("拖拉机")
# c.run("拉货")

# class computer():
#
#     __model = ''
#     __time = 0
#     __color=''
#     __weight = 0
#     __cpu = ''
#     __ram = 0
#     __rom = 0
#     def play(self,name):
#         print("打的游戏为：",name)
#     def work(self):
#         print("正在办公")
# c = computer()
# c.play("植物大战僵尸")
# c.work()


class monkey():
    __sort = ''
    __sex = ''
    __color = ''
    __weight = ''

    def fire(self,materials):
        print('正在使用',materials,'造火')

    def learn(self,something):
        print('正在学习：',something)

m = monkey()
m.fire("木头")
m.learn("电脑")












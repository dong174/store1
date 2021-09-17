import time

# class oldPhone:
#     __brand = ""
#     __username = ""
#     def setUsername(self,username):
#         self.__username=username
#     def setBrand(self,brand):
#         self.__brand=brand
#     def showPhone(self):
#         print("手机牌子为",self.__brand,"的手机很好用")
#     def call(self):
#         print("正在给",self.__username,"打电话")
#
# o = oldPhone()
# o.setUsername("张三")
# o.setBrand("诺基亚")
# o.showPhone()
# o.call()
#
# # class newPhone(oldPhone):
# #     def call(self):
# #         print("语音拨号中。")
# #         for i in range(3):
# #             print(".",end="")
# #             time.sleep(1)
# #         super().call()
# #         super().showPhone()
# #
# # n = newPhone()
# # n.setUsername('李四')
# # n.setBrand("华为")
# # n.call()
#
# class Test(oldPhone):
#     def setBrand(self,brand):
#         self.__brand=brand
#     def test(self):
#         print("新手机牌子为",self.__brand)
#         super().showPhone()
#         super().call()
# t = Test()
# t.setBrand("小米")
# t.setUsername("王五")
# t.test()

# class cook:
#     __name = ""
#     __age = ""
#     # def setName(self,name):
#     #     self.__name=name
#     # def getName(self,name):
#     #     return self.__name
#     # def setAge(self,age):
#     #     self.__age=age
#     # def getAge(self,age):
#     #     return self.__age
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def do(self):
#         print("宫保鸡丁的做法")
#     def show(self):
#         print("我叫",self.__name,"今年",self.__age,"了")
# # c = cook()
# # c.do()
#
# class cook2(cook):
#     def do2(self):
#         print("北京烤鸭的做法")
#
# class cook3(cook2,cook):
#     def do(self):
#         print("宫保鸡丁2的做法")
#     def do2(self):
#         print("北京烤鸭2的做法")
# # co = cook3()
# # co.do()
# # co.do2()
#
# class test(cook2,cook):
#     def __init__(self,name,age):
#         cook.__init__(self,name,age)
#
# t = test("张三","33")
# t.show()
# t.do()
# t.do2()

class people():
    name = ""
    __age = ""
    __sex = ""
    def __init__(self,n,a,s):
        self.name=n
        self.__age=a
        self.__sex=s
    def work(self):
        print("%s岁的%s性%s正在干活"%(self.__age,self.__sex,self.name))

    def sing(self):
        print("%s在唱歌"%(self.name))
    def study(self):
        print("%s在学习"%(self.name))
class worker(people):
    def __init__(self,n,a,s):
        people.__init__(self,n, a, s)
w = worker("张三","33","男")
w.work()

class student(people):
    no = ""
    def __init__(self,n,a,s,no):
        people.__init__(self,n,a,s)
        self.no=no
    def sing(self):
        print("学号为%s的%s在唱歌"%(self.no,self.name))
    def study(self):
        print("学号为%s的%s在学习"%(self.no,self.name))

st = student("李四","32","男","741")
st.sing()
st = student("王五","56","男","8181")
st.study()
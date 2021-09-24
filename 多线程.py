from threading import Thread
import threading
import time

breadNum = 0


class cook(threading.Thread):
    def __init__(self,username):
        threading.Thread.__init__(self)
        self.name = username
        # self.count = count
    def run(self):
        do(self.name)

class customer(threading.Thread):

    def __init__(self,username,count,money):
        threading.Thread.__init__(self)
        self.name = username
        self.count = count
        self.monye = money
    def run(self):
        sale(self.name, self.count,self.monye)


# breadNum = 0
def do(cookName):
    global breadNum
    while breadNum >= 0:
        # time.sleep(0.5)

        breadNum = breadNum + 1

        print(cookName,"做了",breadNum,'个蛋挞')
        if breadNum == 500:
            time.sleep(3)

def sale(customer,saleNum,money):
    global breadNum
    while money:
        # time.sleep(1)
        saleNum = saleNum + 1
        breadNum = breadNum-1
        money = money - 2
        print(customer,"买了",saleNum,"个蛋挞")
        if breadNum == 0:
            time.sleep(2)
        if money == 0:
            break

c1 = cook("张三")
c2 = cook("李四")
c3 = cook("王五")
p1 = customer("老大",0,3000)
p2 = customer("老二",0,3000)
p3 = customer("老三",0,3000)
p4 = customer("老四",0,3000)
p5 = customer("老五",0,3000)
p6 = customer("老六",0,3000)

c1.start()
c2.start()
c3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


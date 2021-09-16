#   水杯

# class water_glass:
#     height = 0
#     volume = 0
#     color = ""
#     material = ""
#     def into(self):
#         print("这是一个高度为",self.height,"cm,颜色为",self.color,
#               ",材料为",self.material,"的,容积为",self.volume,"ml的水杯")
# w = water_glass()
#
# w.color = '黑色'
# w.volume = 500
# w.material = '陶瓷'
# w.height = 30
# w.into()


class computer:
    __username=""
    __screen_size=0
    __price=0
    __cpu=""
    __memory=0
    __time=0
    def showComputer(self):
        print("本电脑详情：屏幕尺寸",self.__screen_size,
              "价格",self.__price,
              "cpu",self.__cpu,
              "内存",self.__memory,
              "待机时长",self.__time)
    def setUsername(self,username):
        self.__username=username

    def setScreen_size(self,screen_size):
        if screen_size < 0:
            print("屏幕尺寸不能小于0")
        else:
            self.__screen_size = screen_size

    def setPrice(self,price):
        if price < 0 :
            print("价格不能小于0")
        else:
            self.__price=price

    def setCpu(self,cpu):
        self.__cpu = cpu

    def setMemory(self,memory):
        if memory < 0:
            print("内存大小不能小于0")
        else:
            self.__memory = memory

    def setTime(self,time):
        if time < 0:
            print("待机时间不能小于0")
        else:
            self.__time = time


    def write(self):
        print(self.__username,"正在使用电脑打字")
    def game(self,gamename):
        print(self.__username,"正在使用电脑打",gamename)
    def look(self,videoname):
        print(self.__username,"正在使用电脑看",videoname)

c = computer()
# c.username = '张三'
c.setUsername("张三")
# c.cpu = 'i5'
c.setCpu('i5')
# c.time = 8
c.setTime(8)
# c.screen_size = 15.6
c.setScreen_size(15.6)
# c.price = 5000
c.setPrice(5000)
# c.memory = 16
c.setMemory(16)

c.showComputer()
c.write()
c.game("CSGO")
c.look("柯南")

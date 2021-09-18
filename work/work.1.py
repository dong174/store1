class Role(object):
    id = '您还没有输入职工编号呦~'
    def __init__(self, name, age, sex, hobby):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__hobby = hobby

    def get_name(self):
        return self.__name
    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0 and age < 150:
            self.__age = age

    def get_sex(self):
        return self.__sex
    def set_sex(self, sex):
        if sex == '男' or sex == '女':
            self.__sex = sex

    def get_hobby(self):
        return self.__hobby
    def set_hobby(self, hobby):
        self.__hobby = hobby

    def play(self):
        print('我叫:{}, 性别:{}, 我今年:{}岁了, 我喜欢:{}。'.format(self.get_name(),
                             self.get_sex(), self.get_age(), self.get_hobby()))

class Employee(Role):
    def __init__(self, name, age, sex, hobby, salary):
        super().__init__(name, age, sex, hobby)
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary

    @staticmethod
    def ID(id):
        id = input('请输入您的职工编号：')
        return id

    def DiaoYong_staticmethod(self):
        self.id = self.ID(id)

    def play(self):
        print('我叫:{}, 职工编号是:{}, 性别:{}, 我今年:{}岁了, 我喜欢:{}, 我的薪资是:{}。'.format(self.get_name(),
                    self.id, self.get_sex(), self.get_age(), self.get_hobby(), self.get_salary()) + '\n')

class Manager(Employee):
    def __init__(self, name, age, sex, hobby, salary, vehicle):
        super().__init__(name, age, sex, hobby, salary)
        self.__vehicle = vehicle

    def get_vehicle(self):
        return self.__vehicle
    def set_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def play(self):
        print('我叫:{}, 职工编号是:{}, 性别:{}, 我今年:{}岁了, 我喜欢:{}, 我的薪资是:{}, '
              '交通工具是:{}。'.format(self.get_name(),self.id, self.get_sex(), self.get_age(),
                                 self.get_hobby(), self.get_salary(), self.get_vehicle()))


if __name__ == '__main__':
    print('Employee测试(调用职工编号)：')
    Cyg = Employee('曹有根', 21, '男', '看动漫', 6000)
    Cyg.DiaoYong_staticmethod()
    Cyg.play()
    print('Manager测试(不调用职工编号)：')
    C_yg = Manager('曹有根', 21, '男', '看动漫', 6000, '私家车')
    # C_yg.DiaoYong_staticmethod()
    C_yg.play()

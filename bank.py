import os

filename = 'bank.txt'


def main():
    while True:
        menu()
        choice = int(input('请输入你想使用的功能'))
        if choice in [1, 2, 3, 4, 5, 6, 0]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                adduser()
            elif choice == 2:
                save_money()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                transfer()
            elif choice == 5:
                search()
            elif choice == 6:
                show()


import random

bank_name = "工商银行起码路分行"


def adduser():
    bank = []
    while True:
        username = input("请输入您的用户名")
        password = input("请输入您的密码")
        print("请输入您的地址")
        country = input("\t\t请输入您的国家")
        province = input("\t\t请输入您的省份")
        street = input("\t\t请输入您的街道")
        door = input("\t\t请输入您的门牌号")
        account = str(random.randint(10000000, 99999999))
        money = int(0)
        userinfo = {'account': account, 'username': username, 'password': password, 'country': country,
                    'province': province, 'street': street, 'door': door, 'money': money, 'bank_name': bank_name}
        bank.append(userinfo)
        if username in bank:
            return 2
        if len(bank) >= 100:
            return 3
        else:
            print('添加用户成功！')
        answer = input('是否继续添加？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(bank)


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def save_money():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as rfile:
            user_old = rfile.readlines()
            # print(user_old)
    else:
        return
    user_account = input('请输入要存款的用户的ID：')
    with open(filename, 'w', encoding='utf-8')as wfile:
        for item in user_old:

            d = dict(eval(item))
            if d['account'] == user_account:
                print('成功找到用户，请输入要存入的钱数：')
                while True:
                    try:
                        a=int(input('请输入存款数量：'))
                        if d['money']=='':
                            d['money'] = a
                        else:
                            d['money']=int(d['money'])+a
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('存款成功！！！')

            else:
                print('没有找到用户信息')
                wfile.write(str(d) + '\n')
    answer = input('是否继续存款？y/n')
    if answer == 'y' or answer == 'Y':
        save_money()


def withdraw():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as rfile:
            user_old = rfile.readlines()
            # print(user_old)
    else:
        return
    user_account = input('请输入要取款的用户的ID：')
    user_password = input('请输入密码：')
    with open(filename, 'w', encoding='utf-8')as wfile:
        for item in user_old:

            d = dict(eval(item))
            # print(d['money'])
            # print(type(d['money']))
            if d['account'] == user_account and d['password'] == user_password:
                print('成功找到用户，请输入要取出的钱数：')
                while True:
                    a = int(input('请输入取款钱数：'))
                    if a <= int(d['money']):
                        d['money'] = int(d['money']) - a
                        print('成功取款，余额为：',d['money'])
                        wfile.write(str(d) + '\n')

                        answer = input('是否继续取款？y/n')
                        if answer == 'y' or answer == 'Y':
                            withdraw()
                        else:
                            break
                    else:
                        print('该用户没有足够的存款')
                        break
            else:
                print('没有找到用户信息')
                wfile.write(str(d) + '\n')

def transfer():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as rfile:
            user_old = rfile.readlines()
            # print(user_old)
    else:
        return
    user1_account = input('请输入转出的用户的ID：')
    user2_account = input('请输入收账的用户ID：')
    with open(filename, 'w', encoding='utf-8')as wfile:
        for item in user_old:

            d1 = dict(eval(item))
            d2 = dict(eval(item))
            if d1['account'] == user1_account :
                print('成功找到用户，请输入要转出的钱数：')
                if d2['account'] == user2_account:
                    while True:
                        a = int(input('请输入转出钱数：'))
                        if a <= int(d1['money']):
                            d1['money'] = int(d1['money']) - a
                            print('成功转账，余额为：', d1['money'])
                            d2['money'] = int(d2['money']) + a
                            wfile.write(str(d1) + '\n')
                            wfile.write(str(d2) + '\n')
                            answer = input('是否继续转账？y/n')
                            if answer == 'y' or answer == 'Y':
                                withdraw()
                            else:
                                break
                        else:
                            print('该转账用户没有足够的存款')
                            break
            else:
                continue
                # print('没有找到用户信息')
                # wfile.write(str(d1) + '\n')
                # wfile.write(str(d2) + '\n')


def search():
    user_query = []
    while True:
        if os.path.exists(filename):
            id = input('请输入需要查询的用户ID：')
            password=input('请输入密码：')
            with open(filename, 'r', encoding='utf-8')as rfile:
                user = rfile.readlines()
                for item in user:
                    d = dict(eval(item))
                    # print(d)
                    if id !='' and password!='':
                        if d['account'] == id and d['password']==password:
                            user_query.append(d)
            show_info(user_query)
            user_query.clear()
            answer = input('是否要继续查询？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('没有找到用户信息')
            return 


def show_info(lst):
    if len(lst) == 0:
        print('没有查询到用户信息，无数据显示！！！')
        return
    format_title = '{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t'
    print(format_title.format('account', '用户名', '密码', '国家', '省份', '街道', '门牌号', '存款', '银行名'))
    format_data = '{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t'
    for item in lst:
        print(format_data.format(item['account'],
                                 item['username'],
                                 item['password'],
                                 item['country'],
                                 item['province'],
                                 item['street'],
                                 item['door'],
                                 item['money'],
                                 item['bank_name']
                                 ))


def show():
    user_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as rfile:
            user = rfile.readlines()
            for item in user:
                user_lst.append(eval(item))
            if user:
                show_info(user_lst)


def menu():
    print('***************************')
    print('*     中国工商银行           *')
    print('*     账户管理系统           *')
    print('*        V1.0             *')
    print('***************************')
    print('*\t\t1.开户             *')
    print('*\t\t2.存钱             *')
    print('*\t\t3.取钱             *')
    print('*\t\t4.转账             *')
    print('*\t\t5.查询             *')
    print('*\t\t6.显示信息          *')
    print('*\t\t0.Bye             *')
    print('**************************')


if __name__ == '__main__':
    main()

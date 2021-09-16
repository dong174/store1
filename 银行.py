print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
import random
import pymysql
import datetime

con = pymysql.connect(host='localhost',user='root',password='root',database='bank')
cursor = con.cursor()

bank={}
bank_name="工商银行七马路分行"
#                 一一对应  ，  不是名称对应
def bank_adduser(account,username,password,country,provice,street,door,money,registerDate,bank_name):
    if  len(bank) >100 :return 3#bank_adduer=3
    if username in bank:return 2#bank_adduer=2

    sql = "insert into users(account,username,password,country,provice,street,door,money,registerDate,bankname) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    a = [account,username,password,country,provice,street,door,money,registerDate,bank_name]
    cursor.execute(sql,a)
    con.commit()
    print(bank)
    return 1#bank_adduer=1


def adduser(money=0, registerDate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,country,province,street,door,money,registerDate,bank_name)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, money, bank_name))
    elif status == 2:
        print('用户已存在')
    elif status == 3:
        print('用户库已满')



def usermoney():

    username=input('请输入您的用户名')
    password = input('输入密码')
    usermoney = input('输入取款金额')
    sql = "update users set money=money-"+usermoney+" where username=%s and password="+password+""
    a = [username]
    cursor.execute(sql,a)
    con.commit()
    sql2 = "select money from users where username=%s"
    b = [username]
    cursor.execute(sql2,b)
    money = cursor.fetchmany(1)
    print(money)

def amunt():

    username=input('请输入您的用户名')
    amunt=input('请输入您要存入的金额')


    sql = "update users set money=money+%s where username=%s"
    a = [amunt, username]
    cursor.execute(sql,a)
    con.commit()
    sql2 = "select money from users where username=%s"
    b = [username]
    cursor.execute(sql2,b)
    money = cursor.fetchmany(1)
    print(money)



def transfer():
    username1= input('请输入付款账户')
    password= input('请输入密码')
    username2= input('请输入收款账户')
    money1=input('请输入转账金额')
    sql1 = "update users set money=money-%s where username=%s and password=%s"
    a =[money1,username1,password]
    cursor.execute(sql1, a)
    sql2 = "update users set money=money+%s where username=%s"
    b = [money1, username2]
    cursor.execute(sql2,b)
    con.commit()
    sql3 = "select money from users where username=%s"
    b = [username1]
    cursor.execute(sql3,b)
    money2 = cursor.fetchmany(1)
    print("付款账户余额为：",money2)
    sql4 = "select money from users where username=%s"
    b = [username2]
    cursor.execute(sql4,b)
    money3 = cursor.fetchmany(1)
    print("收款账户余额为：",money3)



def search():
    username=input('请输入要查询的账户：')
    sql = 'select * from users where username = %s'
    a = [username]
    cursor.execute(sql,a)
    data = cursor.fetchall()
    print(data)
    con.commit()






while True:
    begin=input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、取钱")
        usermoney()
    elif  begin == "3":
        print("3、存钱")
        amunt()
    elif  begin == "4":
        print("4、转账")
        transfer()
    elif  begin == "5":
        print("5、查询 ")
        search()
    elif  begin == "6":
        print("6、退出")
        break



cursor.close()
con.close()
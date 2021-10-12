'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import xlrd
import pymysql
con = pymysql.connect(host='localhost',user='root',password='root',database='HKRtest')
cursor = con.cursor()
# sql = "create table Login (username varchar(20),password varchar(20),exception varchar(20))"
# cursor.execute(sql)
# con.commit()
# con.close()
# wb = xlrd.open_workbook(filename=r"E:\python自动化测试\测试\day03【自动化框架】\HKR.xlsx")
# sheet = wb.sheet_by_name("Login")
# rows = sheet.nrows
# cols = sheet.ncols
# sql1 = "insert into Login(username,password,exception) value(%s,%s,%s)"
# for i in range(1,rows):
#     username = sheet.cell(i, 0).value
#     password = sheet.cell(i, 1).value
#     exception = sheet.cell(i,2).value
#     values = (username,password,exception)
#     cursor.execute(sql1,values)
# cursor.close()
# con.commit()
# con.close()
#
class InitPage:
    loginSuccess_data = []
    loginError_data = []
    # wb = xlrd.open_workbook(filename=r"E:\python自动化测试\测试\day03【自动化框架】\HKR.xlsx")
    # sheet = wb.sheet_by_name("Login")
    # rows = sheet.nrows
    # cols = sheet.ncols
    # title = sheet.row_values(0)
    # for i in range(1, 3):
    #     data = sheet.row_values(i)
    #     data[1] = str(int(data[1]))
    #     login = zip(title, data)
    #     loginSuccess_data.append(dict(login))
    # for i in range(3, 5):
    #     data = sheet.row_values(i)
    #     data[1] = str(int(data[1]))
    #     login = zip(title, data)
    #     loginError_data.append(dict(login))
# ================================================================================
#     sql2 = "select * from Login"
#     cursor.execute(sql2)
#     des = cursor.description
#     a = [item[0] for item in des]
#     print(a)
#     data1 = cursor.fetchall()
#     data = list(data1)
#     print(data)
#     column_list = []
#     for i in data:
#         # 提取字段名，追加到列表中
#         column_list.append(i[0])
#     print(column_list)

    # login_error_data = [
    #     # id : msg_uname
    #     {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]


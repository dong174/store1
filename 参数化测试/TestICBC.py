# from unittest  import TestCase
# from ddt import ddt
# from ddt import data
# from ddt import unpack
# from ICBC import bank_addUser
#
# # username,password,country,province,street,door,money
# da = [
#     ["贾生",123456,"USA","纽约省","林肯大道","s001",8000,1],
#     ["贾生",123456,"USA","纽约省","林肯大道","s001",8000,2],
# ]
#
# @ddt
# class TestICBC(TestCase):
#
#     @data(*da)
#     @unpack
#     def testAddUser(self,a,b,c,d,e,f,g,h):
#         s = bank_addUser(a,b,c,d,e,f,g)
#         self.assertEqual(s,h)



from unittest  import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from ICBC import *
import xlrd

wb=xlrd.open_workbook(filename=r"银行.xlsx")



# #{"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}
# # username,password,country,province,street,door,money
# da1 = [
#     ["贾生",123456,"USA","纽约省","林肯大道","s001",8000,1],
#     ["贾生",123456,"USA","纽约省","林肯大道","s001",8000,2],
# ]
sheets=wb.sheet_by_name('开户')

da1=[sheets.row_values(1),sheets.row_values(2)]


#ac,money

sheets=wb.sheet_by_name('存钱')


da2=[sheets.row_values(1),sheets.row_values(2)]
#
# #bank_takeMoney(account,password,money)

sheets=wb.sheet_by_name('取钱')
rows = sheets.nrows
print(rows)
da3 = []
for i in range(1,rows):
    a = sheets.row_values(i)
    da3.append(a)
print(da3)

# # #bank_selectUser(account,password)

# #
sheets=wb.sheet_by_name('查询')
da4=[sheets.row_values(1),sheets.row_values(2)]

#  #bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney)

sheets=wb.sheet_by_name('转账')
da5=[sheets.row_values(1),sheets.row_values(2)]






@ddt
class TestICBC(TestCase):#运行这个

    @data(*da1)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):
        s = bank_addUser(a,b,c,d,e,f,g)
        self.assertEqual(s,h)

    @data(*da2)
    @unpack
    def testSave(self,a,b,c):
        s=bank_saveMoney(a,b)
        self.assertEqual(s,c)

    @data(*da3)
    @unpack
    def testTake(self,a,b,c,d):
        s=bank_takeMoney(a,b,c)
        self.assertEqual(s,d)

    @data(*da4)
    @unpack
    def testSelect(self,a,b,c):
        s=bank_selectUser(a,b)
        self.assertEqual(s,c)

    @data(*da5)
    @unpack
    def testTrans(self,a,b,c,d,e):
        s=bank_transformMoney(a,b,c,d)
        self.assertEqual(s,e)













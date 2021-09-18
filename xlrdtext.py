import xlrd
import pymysql
import xlwt
from xlrd import xldate_as_tuple
wb = xlrd.open_workbook(filename=r"E:\python自动化测试\python\课程\day8【xlrd】\资料\2020年每个月的销售情况.xlsx")

number = 0
sum = 0
money = 0
def sale(month,name1):
    global sum
    global money
    money1 = 0
    sheet = wb.sheet_by_name(str(month)+"月")
    rows = sheet.nrows  # 获取有多少行
    for i in range(1,rows):
        data = sheet.row_values(i)
        name = sheet.cell_value(i, 1)
        sum = sum + data[2] * data[4]
        if name == name1:
            money = money+data[2] * data[4]
            money1 = money1 + data[2] * data[4]
    if name1 == "羽绒服":
        print(name1,"的",month,"月的销售额为：",round(money1,2),"本月销售额占全年销售总额的比重为",'%.2f'%(money1/sum*100),"%")
    elif name1 == "牛仔裤":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "皮衣":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "皮草":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "衬衫":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "风衣":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "T血":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "马甲":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")
    elif name1 == "小西装":
        print(name1, "的", month, "月的销售额为：", round(money1, 2), "本月销售额占全年销售总额的比重为", '%.2f' % (money1 / sum * 100), "%")

for i in range(1,13):
    sale(i,"羽绒服")
yumoney = money
print("本年度羽绒服销售总额为：",round(yumoney,2),"占全年销售总额的比重为", '%.2f' % (yumoney / sum * 100), "%")

money = money - yumoney
for i in range(1,13):
    sale(i,"牛仔裤")
niumoney = money
print("本年度牛仔裤销售总额为：",round(niumoney,2),"占全年销售总额的比重为", '%.2f' % (niumoney / sum * 100), "%")

money = money - niumoney
for i in range(1,13):
    sale(i,"皮衣")
pmoney = money
print("本年度皮衣销售总额为：",round(pmoney,2),"占全年销售总额的比重为", '%.2f' % (pmoney / sum * 100), "%")

money = money - pmoney
for i in range(1,13):
    sale(i,"皮草")
pimoney = money
print("本年度皮草销售总额为：",round(pimoney,2),"占全年销售总额的比重为", '%.2f' % (pimoney / sum * 100), "%")

money = money - pimoney
for i in range(1,13):
    sale(i,"T血")
tmoney = money
print("本年度T血销售总额为：",round(tmoney,2),"占全年销售总额的比重为", '%.2f' % (tmoney / sum * 100), "%")

money = money - tmoney
for i in range(1,13):
    sale(i,"衬衫")
cmoney = money
print("本年度衬衫销售总额为：",round(cmoney,2),"占全年销售总额的比重为", '%.2f' % (cmoney / sum * 100), "%")

money = money - cmoney
for i in range(1,13):
    sale(i,"风衣")
fmoney = money
print("本年度风衣销售总额为：",round(fmoney,2),"占全年销售总额的比重为", '%.2f' % (fmoney / sum * 100), "%")

money = money - fmoney
for i in range(1,13):
    sale(i,"马甲")
mmoney = money
print("本年度马甲销售总额为：",round(mmoney,2),"占全年销售总额的比重为", '%.2f' % (mmoney / sum * 100), "%")

money = money - mmoney
for i in range(1,13):
    sale(i,"小西装")
xmoney = money
print("本年度小西装销售总额为：",round(xmoney,2),"占全年销售总额的比重为", '%.2f' % (xmoney / sum * 100), "%")
print("全年销售总额：￥",round(sum,2),)

def numberSale(month, name1):
    global number

    number1 = 0
    sheet = wb.sheet_by_name(str(month) + "月")
    rows = sheet.nrows
    for i in range(1, rows):
        data = sheet.row_values(i)
        name = sheet.cell_value(i, 1)
        if name == name1:
            number = number + data[4]
            number1 = number1 + data[4]

    # print("本年度迄今为止的", name1, "销售件数", number)
    if name1 == "羽绒服":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f'%(number1/ 2181*100), "%")
    elif name1 == "牛仔裤":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为",'%.2f' % ( number1 / 4373*100), "%")
    elif name1 == "皮衣":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为",'%.2f' % ( number1 / 303*100), "%")
    elif name1 == "皮草":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f' % (number1 / 2049 * 100), "%")
    elif name1 == "T血":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f' % (number1 / 4809 * 100), "%")
    elif name1 == "衬衫":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f' % (number1 / 1683 * 100), "%")
    elif name1 == "风衣":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f' % (number1 / 2974 * 100), "%")
    elif name1 == "马甲":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f' % (number1 / 120 * 100), "%")
    elif name1 == "小西装":
        print(month, "月", name1, "的销售件数为：", number1, "占本年度的销售占比为", '%.2f' % (number1 / 131 * 100), "%")
    # try:
    #     if number != 0:
    #         print("销售件数占年比为：", '%.2f' % (number1 / number * 100), "%")
    # except:
    #     print("无法计算占比")


for i in range(1, 13):
    numberSale(i, "羽绒服")
yunum = number
print("今年羽绒服的销售总件数为：", yunum)

number = number - yunum
for i in range(1, 13):
    numberSale(i, "牛仔裤")
niunum = number
print("今年牛仔裤的销售总件数为：", niunum)

number = number - niunum
for i in range(1, 13):
    numberSale(i, "皮衣")
pinum = number
print("今年皮衣的销售总件数为：", pinum)

number = number - pinum
for i in range(1, 13):
    numberSale(i, "皮草")
picnum = number
print("今年皮草的销售总件数为：", picnum)

number = number - picnum
for i in range(1, 13):
    numberSale(i, "T血")
tnum = number
print("今年T血的销售总件数为：", tnum)

number = number - tnum
for i in range(1, 13):
    numberSale(i, "衬衫")
cnum = number
print("今年衬衫的销售总件数为：", cnum)

number = number - cnum
for i in range(1, 13):
    numberSale(i, "风衣")
fnum = number
print("今年风衣的销售总件数为：", fnum)

number = number - fnum
for i in range(1, 13):
    numberSale(i, "马甲")
mnum = number
print("今年马甲的销售总件数为：", mnum)

number = number - mnum
for i in range(1, 13):
    numberSale(i, "小西装")
xnum = number
print("今年小西装的销售总件数为：", xnum)

totalnum = yunum + niunum + pinum + picnum+ tnum + cnum + fnum + mnum + xnum
print("本年度销售总件数为：",totalnum)
print("羽绒服的年销售占比为：",'%.2f' % (yunum / totalnum * 100), "%")
print("牛仔裤的年销售占比为：",'%.2f' % (niunum / totalnum * 100), "%")
print("皮衣的年销售占比为：",'%.2f' % (pinum / totalnum * 100), "%")
print("皮草的年销售占比为：",'%.2f' % (picnum / totalnum * 100), "%")
print("T血的年销售占比为：",'%.2f' % (tnum / totalnum * 100), "%")
print("衬衫的年销售占比为：",'%.2f' % (cnum / totalnum * 100), "%")
print("风衣的年销售占比为：",'%.2f' % (fnum / totalnum * 100), "%")
print("马甲的年销售占比为：",'%.2f' % (mnum / totalnum * 100), "%")
print("小西装的年销售占比为：",'%.2f' % (xnum / totalnum * 100), "%")

#数据库导入数据==================================================================================================================================
# con = pymysql.connect(host="localhost",user="root",password="root",database="excel_sale")
# cursor = con.cursor()
#创建数据表
# for i in range(1,13):
#     sql = "create table "+str(i)+"month (day varchar(10),name varchar(10),price varchar(20),inventory_num varchar(20),sale_num varchar(20) )"
#     cursor.execute(sql)
#     con.commit()
# cursor.close()
# con.close()
# def insert(month):
#     sheet = wb.sheet_by_name(str(month)+"月")
#     # for month in range(1,13):
#     sql = "insert into "+str(month)+"month(day,name,price,inventory_num,sale_num) values(%s,%s,%s,%s,%s)"
#     for r in range(1,sheet.nrows):
#         day = sheet.cell(r, 0).value
#         name = sheet.cell(r, 1).value
#         price = sheet.cell(r, 2).value
#         inventory_num = sheet.cell(r, 2).value
#         sale_num = sheet.cell(r, 4).value
#         values = (day, name, price, inventory_num, sale_num)
#         # 执行sql语句
#         cursor.execute(sql, values)
# for i in range(1,13):
#     insert(i)
#     print("成功导入",i,"月份数据")
# cursor.close()
# con.commit()
# con.close()

#数据库导出到excel========================================================================================================
# def export_excel(table_name):
#     conn = pymysql.connect(host="localhost",user="root",password="root",database="company")
#     cur = conn.cursor()  # 建立游标
#     sql = 'select * from %s;' %table_name
#     cur.execute(sql)  # 执行mysql
#     fileds = [filed[0] for filed in cur.description]  # 列表生成式，所有字段，获取表头
#     all_data = cur.fetchall() #所有数据
#     #写excel
#     book = xlwt.Workbook() #先创建一个book
#     sheet = book.add_sheet("三国创业") #创建一个sheet表
#
#     for col, field in enumerate(fileds): #写表头
#         sheet.write(0, col, field)
#     #从第一行开始写
#     row = 1 #行数
#     for data in all_data:  #二维数据，有多少条数据，控制行数
#         for col, field in enumerate(data):  #控制列数
#             sheet.write(row, col, field)
#         row += 1 #每次写完一行，行数加1
#     book.save('%s.xls' %table_name) #保存excel文件
#
# if __name__=='__main__':
#     export_excel('t_employees')

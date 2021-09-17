import xlrd

wb = xlrd.open_workbook(filename=r"E:\python自动化测试\python\课程\day8【xlrd】\资料\2020年每个月的销售情况.xlsx")

sheet = wb.sheet_by_name("1月")

cols = sheet.ncols  # 获取有多少列
rows = sheet.nrows # 获取有多少行
# for j in range(0,cols):
#     print(sheet.col_values(j))
#
#
#
for  i in range(0,rows):
    data = sheet.row_values(i)
    print(data)










# 5.显示当前表数据
import xlrd
url=r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
xl=xlrd.open_workbook(filename=url)

sheet1=xl.sheet_by_index(0)
print(sheet1)
nrows=sheet1.nrows
ncols=sheet1.ncols
# 方法一
for i in range(nrows):
     print(sheet1.row(i))
     print(sheet1.row_values(i,1,2)[0])
# 方法二

for i in range(nrows):
    for j in range(ncols):
        print(sheet1.cell_value(i,j),end='\t')
    print()
# 打开excel表，读取所有表单名
import xlrd
# 1. 打开目的excel表
url=r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
xl=xlrd.open_workbook(filename=url)

# sheet_names()返回列表，列表内容所有表单名
# 2.返回所有表单名
names=xl.sheet_names()
print(names,'返回值类型：',type(names))

# sheet_by_name(parm) 打开指定名的列表
# 3.打开指定表
table1=xl.sheet_by_name('1月')
print(table1,"返回值类型：",type(table1))
# 4.返回有效行数和有效列数，输出打印
nrows=table1.nrows
nclos=table1.ncols
print(nrows,'\t',type(nrows),"\t",nclos)
# 6.显示2020年1-12月的各月季度报表
import xlrd


def sumSale(x):
    url = r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
    xl = xlrd.open_workbook(filename=url)
    sheet1=xl.sheet_by_index(x)
    nrows=sheet1.nrows

    sum=0
    for i in range (1,nrows):
        a=sheet1.cell_value(i,2)
        b=sheet1.cell_value(i,4)

        sum=sum+a*b
    print('2021年%2s月总营销额为：%10.2f'%(x+1,sum))
for j in range(12):
    sumSale(int(j))


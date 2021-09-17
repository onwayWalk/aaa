# 8.2020年各月日销售额
import  xlrd
def avgSale(x):
    url = r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
    xl = xlrd.open_workbook(filename=url)
    sheet1=xl.sheet_by_index(x)
    nrows=sheet1.nrows

    sum=0
    for i in range (1,nrows):
        a=sheet1.cell_value(i,2)
        b=sheet1.cell_value(i,4)

        sum=sum+a*b
        avg=sum/(nrows-1)
    return(avg)
for i in range(12):
    avg=avgSale(i)
    print('2021年%2s月平均日营销额为：%10.2f'%(i+1,avg))

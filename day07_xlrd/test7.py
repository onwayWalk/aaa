# 全年总销售额
import xlrd


def sumSale(x):
    url = r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
    xl = xlrd.open_workbook(filename=url)
    sheet1=xl.sheet_by_index(x-1)
    nrows=sheet1.nrows

    sum=0
    for i in range (1,nrows):
        a=sheet1.cell_value(i,2)
        b=sheet1.cell_value(i,4)

        sum=sum+a*b
    return sum
    # print('2021年%2s月总营销额为：%10.2f'%(x,sum))
sum=0
for j in range(1,13):
    sum+=sumSale(int(j))
print("2020年总营业额:%10.2f"%sum)
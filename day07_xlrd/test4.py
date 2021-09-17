# 7.显示2020年第一季度总营业额
import  xlrd
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
    return(sum)
quarter1=sumSale(2)+sumSale(3)+sumSale(4)
print("2020年第一季度总营业额：%10.2f"%quarter1)
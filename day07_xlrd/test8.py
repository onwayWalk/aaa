# 每件衣服的年销售销售（件数）占比
import  xlrd
def sumSale(y):
    url = r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
    xl = xlrd.open_workbook(filename=url)
    sum1 = sum2 = 0
    for x in range(1,13):
        sheet1=xl.sheet_by_index(x-1)
        nrows=sheet1.nrows

        for i in range (1,nrows):

            sum1+=sheet1.cell_value(i,4)
            a=sheet1.cell_value(i,1)
            if a ==y:
                print(sheet1.cell_value(i, 4), end="\t")
                sum2+=sheet1.cell_value(i,4)
    avg=(sum2/sum1)*100

    print(sum1,'\t',sum2)
    return y,avg
#
def each():
    url = r'C:\Users\lenovo\Desktop\python\day07_xlrd\2020年每个月的销售情况.xlsx'
    xl = xlrd.open_workbook(filename=url)
    list1 = []
    for x in range(1,13):
        sheet1 = xl.sheet_by_index(x - 1)
        nrows = sheet1.nrows

        for i in range(1, nrows):
            if sheet1.cell_value(i,1) not in list1:
                list1.append(sheet1.cell_value(i,1))
    return list1

for i in each():

    print('2020年%5s年销售量占比%4.2f'%sumSale(i),'%')
print('------------------------------------')
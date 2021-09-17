# 最畅销的衣服
# 每件衣服的年销售销售（件数）占比
import  xlrd
def sumSale(y,dict):
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

                sum2+=sheet1.cell_value(i,4)


    dict[y]=sum2

    return dict
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
dict={}
for i in each():
    sumSale(i,dict)
print(dict,type(dict))
a=max(dict.values())
b=min(dict.values())
for i in dict:
    if dict[i]==a:
        print("全年销量最好的衣服是：%-5s销售%5s件" % (i, a))
    if dict[i]==b:
        print("全年销量最差的衣服是：%-5s销售%5s件" % (i, b))

print('------------------------------------')
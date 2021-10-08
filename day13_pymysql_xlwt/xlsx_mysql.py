import xlrd
import pymysql
import os
url='ICBC.xlsx'
xl=xlrd.open_workbook(url,encoding_override='utf-8')

sheet=xl.sheet_by_index(0)
n=sheet.nrows
db=pymysql.connect(host='localhost', user='root', password='123456', database='xlsx', charset='utf8')
cursor=db.cursor()


for i in range (0,n):
    list = []
    for j in range(0,sheet.ncols):

        a=sheet.cell_value(i,j)

        list.append(a)
    print(list)
    sql='insert  into xl values (%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql,list)
    db.commit()
cursor.close()
db.close()
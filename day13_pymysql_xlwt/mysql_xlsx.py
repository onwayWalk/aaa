import xlrd
import xlwt
import pymysql
import copy
import os

db=pymysql.connect(host='localhost', user='root', password='123456', database='xlsx', charset='utf8')
cursor=db.cursor()
sql='select * from xl'
cursor.execute(sql)
a=cursor.fetchall()
print(a)
cursor.close()
db.close()

xlwt=xlwt.Workbook(encoding='utf-8')

sheet=xlwt.add_sheet('sheet1')
for i in range(len(a)):
    for j in range(len(a[i])):
        sheet.write(i,j,label=a[i][j])

xlwt.save('ICBC.xls')
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
name={}
for i in range(len(names)):
    name[names[i][0]]={'年龄':'','性别':'','编号':'','任职公司':'','薪资':'','部门编号':''}
    k=0
    for j in name[names[i][0]]:
        name[names[i][0]][j]=names[i][k+1]
        k+=1
print(name)





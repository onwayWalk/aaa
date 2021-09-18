# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

list1=['羽绒服','牛仔裤','风衣','皮草','T血','衬衫','牛仔裤','羽绒服','牛仔裤','羽绒服','牛仔裤','皮草','T血','风衣','牛仔裤',
       'T血','羽绒服','风衣','T血','牛仔裤','皮草','风衣','T血','牛仔裤','T血','风衣','皮草','羽绒服','T血','风衣']
list2=[253.6,86.3,96.8,135.9,65.8,49.3,86.3,253.6,86.3,253.6,86.3,135.9,65.8,96.8,86.3,65.8,
       253.6,96.8,65.8,86.3,135.9,96.8,65.8,86.3,65.8,96.8,135.9,253.6,65.8,96.8]
list3=[10,60,43,63,63,120,72,69,35,140,90,24,45,25,60,129,10,43,63,60,63,60,58,140,48,43,57,10,63,78]
print(list1)
print(list2)
print(list3)
i=0
ys=ns=fs=ps=ts=cs=0
while len(list1)>i:
    if list1[0]==list1[i]:
        ys+=list3[i]
    if list1[1]==list1[i]:
        ns+=list3[i]
    if list1[2] == list1[i]:
        fs += list3[i]
    if list1[3] == list1[i]:
        ps += list3[i]
    if list1[4]==list1[i]:
        ts+=list3[i]
    if list1[5]==list1[i]:
        cs+=list3[i]
    i=i+1
ss=ys*list2[0]+ns*list2[1]+fs*list2[2]+ps*list2[3]+ts*list2[4]+cs*list2[5]
print("当月总销售额：",round(ss,2))
print("---------------------")
print("当月羽绒服平均日销售量：",round(ys/30,2), ",月销售占比：",round(ys/(ys+ns+fs+ps+ts+cs),2))
print("当月牛仔裤平均日销售量：",round(ns/30,2), ",月销售占比：",round(ns/(ys+ns+fs+ps+ts+cs),2))
print("当月风衣平均日销售量：",round(fs/30,2), ",月销售占比：",round(fs/(ys+ns+fs+ps+ts+cs),2))
print("当月皮草平均日销售量：",round(ps/30,2), ",月销售占比：",round(ps/(ys+ns+fs+ps+ts+cs),2))
print("当月T恤平均日销售量：",round(ts/30,2), ",月销售占比：",round(ts/(ys+ns+fs+ps+ts+cs),2))
print("当月衬衫平均日销售量：",round(cs/30,2), ",月销售占比：",round(cs/(ys+ns+fs+ps+ts+cs),2))





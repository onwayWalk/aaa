# 编程实现99乘法表的倒叙打印
i=9
j=1
while i>0:
    while j<=i:
        print("%d*%d=%d"%(j,i,j*i),end=",")
        j+=1
    j=1
    print()
    i-=1
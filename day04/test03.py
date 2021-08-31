# 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# 返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
import random


def tongji(x):
    y={}
    for i in x:
        if i not in y:
            y[i]=1
        else :
            y[i]=y[i]+1
    return y

# a=[1,1,1,1,1,2,2,2,2,22,3,3,3,3,33,3,4,4,4,4,4,4,4]
# for i in range (30):
#     a.append(random.randint(0,10))
def shuzu(a,b,c):
    shuz=[]
    for i in range(0,a):
        shuz.append(random.randint(b,c))
    return shuz
a=int(input("请输入列表长度："))
print('请输入取值区间（空格隔开）：')
b,c=map(int,input().split())

c=tongji(shuzu(a,b,c))

print(str(c))

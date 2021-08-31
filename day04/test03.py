# 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# 返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
def tongji(x):
    y={}
    for i in x:
        if i not in y:
            y[i]=1
        else :
            y[i]=y[i]+1
    return y
a=[1,1,1,1,1,2,2,2,2,22,3,3,3,3,33,3,4,4,4,4,4,4,4]
c=tongji(a)
print(str(c))

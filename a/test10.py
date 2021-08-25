# 一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，
# 晚上下滑2米，问第几天能出来？请编程求出。
a=t=0
while a<=20:
    a=a+3
    if a>=20:
        break
    else:
        a-=2
    t+=1
print("qing wa pa le %d mi,yong le %d tian"%(a,t))
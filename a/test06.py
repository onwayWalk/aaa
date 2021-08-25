# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
print("qing shu ru zhang hao mi ma")
a,b=input().split()
i=1
username="root"
password="admin"
while 1:
    if username==a and password==b:
        print("deng lu cheng gong ")
        break
    elif i==3:
        print("yong hu suo ding !")
        break
    else:
        print("deng lu shi bai : qing chong xin shu ru :")
        a, b = input().split()
    i += 1

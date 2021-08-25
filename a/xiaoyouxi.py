import random
print("请输入一个数")
a=int(input())
b=random.randint(0,10)
while a!=b:
    if a>b:
        print("猜大了噢，再猜一次吧")
        a=int(input())
    else:
        print ("猜小了哦，再猜一次吧")
        a=int(input())
print ("太棒了，猜对了！")



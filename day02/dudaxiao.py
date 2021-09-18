import random
print ("----------欢迎来到悄悄电玩城，设备还在完善中，可以玩猜大小游戏哦！有惊喜好礼相送----------")
print("请投入游戏币")
money=int(input())
a=int(input("请输入你猜的数！"))
b=random.randint(1,100)
while money>0:
    if a!=b:
        if a>b:
            print("您猜大了呢，离大奖只剩一步了!")
        else :
            print("您猜小了呢，离大奖只剩一步了！")
        print("继续猜吧，马上就中了，请输入是或者否")
        c = input()
        if c == "是":
            a = int(input("请输入你猜的数！"))
        else:
            break
    else :
        print("啊啊啊！恭喜您获得极品美女一枚！")
        break
    money-=1
print("你现在还剩",money,"游戏币")
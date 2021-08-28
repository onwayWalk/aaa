import random

money=input("兄弟，准备了多少钱逛超市啊：")
money=int(money)

# 准备商品
shop={"机械革命":5000,"苹果电脑":15000,"老干妈":15,"卫龙":4.5,"洗衣粉":20,"大西瓜":5}
# 准备购物优惠券
# 机械革命 9折 10zhang  1-10hao
# 老干妈1折    20张      11-30
# 卫龙优2折    15张     30-45
youhui=random.randint(1,46)
print(youhui)
youhuiNum=1#

myshop=[]
# 展示商品
print("--------商品列表-------")
print("名称------单价/元")
for key in shop:
    print(key, shop[key])
print("---------------------")
while True:
    shopid=input("请输入要购买的商品：")

    if shopid not in shop and shopid!="q" and shopid!="Q":
        print("对不起，您输入商品不存在！别瞎弄！")
    elif shopid=="q" or shopid=="Q":
        print("欢迎下次光临！")
        break
    else:
        if money<shop[shopid]:
            print("穷鬼，对不起，钱不够，到其他地方买去！")
        else:
            if youhuiNum>0:
                if youhui<=10 and shopid=="机械革命":
                    myshop.append(shopid)
                    money=money-shop[shopid]*0.9
                    print("恭喜，成功添加购物车!,您的余额还剩：￥",money)
                    youhuiNum-=1
                elif youhui>30 and shopid=="卫龙":
                    myshop.append(shopid)
                    money = money - shop[shopid] * 0.2
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)
                    youhuiNum -= 1
                elif youhui>10 and youhui<=30 and shopid=="老干妈":
                    myshop.append(shopid)
                    money = money - shop[shopid] * 0.1
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)
                    youhuiNum -= 1
                else:
                    myshop.append(shopid)
                    money = money - shop[shopid]
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)

            else:
                myshop.append(shopid)
                money = money - shop[shopid]
                print("恭喜，成功添加购物车!,您的余额还剩：￥", money)

print("----------------qiaoqiaoShop------------------")
s1=s2=s3=s4=s5=s6=0
for i in range(0,len(myshop)):
    if myshop[i]=="机械革命":
        s1+=1
    elif myshop[i]=="苹果电脑":
        s2+=1
    elif myshop[i]=="老干妈":
        s3+=1
    elif myshop[i]=="卫龙":
        s4+=1
    elif myshop[i]=="洗衣粉":
        s5+=1
    elif myshop[i]=="大西瓜":
        s6+=1
print("商品名称","数量")
if "机械革命" in myshop:
    print("机械革命",s1)
if "苹果电脑" in myshop:
    print("苹果电脑",s2)
if "老干妈" in myshop:
    print("老干妈",s3)
if "卫龙" in myshop:
    print("卫龙",s4)
if "洗衣粉" in myshop:
    print("洗衣粉",s5)
if "大西瓜" in myshop:
    print("大西瓜",s6)
print("您的余额还剩：￥", money,)
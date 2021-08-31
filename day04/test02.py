# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典

Friuts={
    "苹果":32.8,
    "香蕉":22,
    "葡萄":15.5,
    "草莓":88,
    "樱桃":33.3,
    "桃子":2.2
}
info={"小明":{
    'friuts':{'苹果':4,'草莓':10,'香蕉':5},
            },
      "小刚":{
    'friuts':{'葡萄':11,'橘子':10,'樱桃':6}
            }
    }
for a in info:
    money = 0
    for i in info[a]['friuts']:
        if i in Friuts:
            money+=Friuts[i]*info[a]['friuts'][i]
    info[a]['money']=money
print(str(info))





class Air_conditioner:

    __name=''
    __price=0

    def setname(self,value):
        self.__name=value

    def setprice(self,value):
        self.__price=value

    def getname(self):
        return self.__name

    def getprice(self):
        return self.__price

    def power_on(self):
        print("air_conditioner开机啦！")

    def power_off(self,value):
        print("air_conditioner将在%s分钟之后关机！"%value)

    def jie(self):
        print("air conditioner \n品牌名称：%s\n价格：%s￥"%(self.__name,self.__price))

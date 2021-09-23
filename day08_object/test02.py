class test02:
    __screen_size=0
    __price=0
    __cpu=''
    __memory_size=0
    __standby_time=0
    def setSC(self,v):
        self.__screen_size=v
    def setprice(self,v):
        self.__price=v
    def setcpu(self,v):
        self.__cpu=v
    def setmeory(self,v):
        self.__memory_size=v
    def setstandby(self,v):
        self.__standby_time=v
    def getSC(self):
        return self.__screen_size
    def getprice(self):
        return self.__price
    def getcpu(self):
        return  self.__cpu
    def getmemory(self):
        return  self.__memory_size
    def getstandby(self):
        return  self.__standby_time

    def typing(self):
        print("我可以用来打字")
    def play_games(self):
        print("我可以用来打游戏")
    def play_vidio(self):
        print("我可以用来看视频")
    def introduce(self):
        print("这款电脑屏幕%s寸，价格：%s￥，CPU型号：%s，内存大小%sG，待机时长%s小时"%(self.__screen_size,self.__price,self.__cpu,self.__memory_size,self.__standby_time))

a=test02()
a.setSC(32)
a.setcpu('Core-i7')
a.setmeory(20)
a.setprice(18000)
a.setstandby(10)
a.typing()
a.introduce()
from typing import Any


class test1:
    __v=0
    __xing=''
    __cai=''
    __color=''
    __high=''
    def getv(self):
        return self.__v
    def setv(self,v):
        if v<=0:
            print("体积不能为0L或小于0升")
        else:
            self.__v=v
    def getxing(self):
        return  self.__xing
    def getcai(self):
        return  self.__cai
    def getcolor(self):
        return self.__color
    def gethigh(self):
        return  self.__high
    def setxing(self,v):
        self.__xing=v
    def setcai(self,v):
        self.__cai=v
    def setcolor(self,v):
        self.__color=v
    def sethigh(self,v):
        if v>0:
            self.__high=v
        else:
            print("高度需要大于0cm")
    def cun(self,p,m):
        if str(m).isdigit() is False:
            print('请输入正确的格式')
        elif int(m)>2 or int(m)<0:
            print("你放多了或者放少了")
        else:
            print("该杯子存放了%s%s升"%(p,m))
    def jie(self):
        print("这款杯子体积：%s，形状：%s，材质：%s,颜色：%s,高：%s"%(self.__v,self.__xing,self.__cai,self.__color,self.__high))
a=test1()
a.setcai("黄金")
a.setv(2)
a.sethigh(20)
a.setcolor('绿色')
a.setxing('五角形')
a.cun('人参鹿茸汤','2')
a.jie()


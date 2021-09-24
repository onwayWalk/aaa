from threading import  Thread
import time

box=500
boxN=0
cus=6
class cook(Thread):
    name=''
    def run(self) -> None:
        while True:
            global box,boxN,cus

            if boxN<box:
                boxN+=1
                print("%s做了一个蛋挞！,现在有%s个"%(self.name,boxN))
            else:
                if cus>0:
                    time.sleep(0.01)
                    print("%s休息了三分钟"%self.name)
                else:
                    break
class customer(Thread):
    name=''
    money=2000
    def run(self) -> None:
        while True:
            global box,boxN,cus
            if boxN>0 :
                if self.money>0:
                    self.money-=2
                    boxN-=1
                    print("%s买了一个蛋挞！,还剩%s￥"%(self.name,self.money))
                else:
                    cus-=1
                    print("%s没钱了要走了"%self.name)
                    break
            else:
                time.sleep(0.01)
                print("%s休息了两分钟，还想吃！"%self.name)
c1=cook()
c2=cook()
c3=cook()
c1.name="张三"
c2.name="李四"
c3.name="wa"

cu1=customer()
cu2=customer()
cu3=customer()
cu4=customer()
cu5=customer()
cu6=customer()
cu1.name="1号"
cu2.name="2号"
cu3.name="3号"
cu4.name="4号"
cu5.name="5号"
cu6.name="6号"

c1.start()
c2.start()
c3.start()
cu1.start()
cu2.start()
cu3.start()
cu4.start()
cu5.start()
cu6.start()

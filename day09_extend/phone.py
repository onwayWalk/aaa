import time
class Oldphone:
    __name=''
    __phoneNum=''
    __addr=''
    def setname(self,name):
        self.__name=name
    def setphoneNum(self,phoneNum):
        self.__phoneNum=phoneNum
    def setaddr(self,addr):
        self.__addr=addr
    def getname(self):
        return self.__name
    def getphoneNum(self):
        return  self.__phoneNum
    def getaddr(self):
        return self.__addr

    def call_on(self,phoneNum):
        print("正在向%s拨号中\n(%s)"%(phoneNum,self.__addr))
        for i in range(6):
            print('.',end='')
            time.sleep(0.5)
        print()
        print('已接通')
    def call_off(self,second):
        for i in range(second):
            time.sleep(1)
        print("通话关闭")
class Smartphone(Oldphone):
    __photo=''
    __audio_record=False

    def setphoto(self,photo):
        self.__photo=photo

    def setaudio_record(self,audio_record):
        self.__audio_record=audio_record

    def call_on(self,phoneNum):
        Oldphone.call_on(self,phoneNum)

        print('头像:%s'%self.__photo)

        if bool(self.__audio_record) is True:
            print("录音功能已经启动")
# old=Oldphone()
# old.setname("小灵通")
# old.setphoneNum('18438595765')
# old.setaddr('河南（移动）')
# old.call_on(15514819276)
# old.call_off(10)
new=Smartphone()
new.setname("苹果8")
new.setphoneNum('18438595765')
new.setaddr('河南（移动）')
new.setphoto("大鼻子露珠")
new.setaudio_record('True')
new.call_on(1121321321312)

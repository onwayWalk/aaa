class Student:
    __name=''
    __age=0
    def setname(self,value):
        self.__name=value
    def setage(self,value):
        if str(value).isdigit is False:
            print("请修改原代码，你输入的格式非法！")
        elif int(value)<=0 or int(value)>100:
            print('你输入的大小不在正常范围内！')
        else:
            self.__age=value

    def getname(self):
        return  self.__name
    def getage(self):
        return  self.__age

    def showMe(self):
        print("大家好，我叫%s，今年%ss岁了！"%(self.__name,self.__age))
    def company(self,Stu):
        if self.__age>Stu.__age:
            print("我比%s大%s岁！"%(Stu.__name,self.__age-Stu.__age))
        elif self.__age<Stu.__age:
            print("我比%s小%s岁！"%(Stu.__name,Stu.__age-self.__age))
        else:
            print("我和%s一样大"%Stu.__name)
s1=Student()
s1.setname("张三")
s1.setage(15)
s1.showMe()
s2=Student()
s2.setname("李四")
s2.setage(18)
s2.showMe()
s1.company(s2)
s2.company(s1)
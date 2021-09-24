class low_cook:
    __name=''
    __age=''
    def setname(self,name):
        self.__name=name
    def setage(self,age):
        self.__age=age
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def steam_rice(self):
        pass
class intermediate_cook(low_cook):
    def cooking(self):
        pass
class senior_cook(intermediate_cook):
    def steam_rice(self):
        print("我会蒸饭")
    def cooking(self):
        print("我会炒菜")

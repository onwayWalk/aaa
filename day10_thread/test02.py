from threading import  Thread

class kill(Thread):
    name=''
    def run(self) -> None:
        name=self.name
        for i in range(1,100):
            print("%s杀死了%s病毒"%(name,i))

a=kill()
a.name='360'

b=kill()
b.name='电脑管家'
a.start()
b.start()
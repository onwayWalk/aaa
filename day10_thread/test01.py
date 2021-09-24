ticket=500
from threading import  Thread
import threading
lock1=threading.Lock()

class User(Thread):
    username=''
    count=0
    def run(self) -> None:
        while True:
            global ticket,lock
            lock1.acquire()
            if ticket>0:

                ticket=ticket-1


                self.count=self.count+1


                print("%s抢了一张票，还剩%s张票！"%(self.name,ticket))


            else:

                print("%s抢了%s张票!" % (self.name, self.count))

                break
            lock1.release()

user1=User()
user1.name='张三'
user2=User()
user2.name="李四"
user3=User()
user3.name="王五"
user1.start()
user2.start()
user3.start()


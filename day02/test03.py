# 使用random模块，如何产生 50~150之间的数？
import random
i=0
while i<100:
    i+=1
    a = random.randint(50, 150)
    print(a)

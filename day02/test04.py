# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
print("qing shu ru san jiao xing de san tiao bian chang du:")
a,b,c=map(int,input().split())
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("gai san liao bian ke yi gou cheng san jiao xing")
        if a==b!=c or a==c!=b or b==c!=a:
            print ("deng yao san jiao xing ")
        elif a==b==c:
            print ("deng bian san jiao xing ")
        else:print("pu tong san jiao xing ")
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print("zhi jiao san jiao xing ")
    else:print('bu neng gou cheng san jiao xing ')
else:print("bu neng gou cheng san jiao xing ")
# 实现输入10个数字，并打印10个数的求和结果
print("请输入需要求和的十个整数")
# ---------多输入方法---------
# 方法一
# 依次输入多个数可以使用a,b,c=input("").split(,)
# 方法二
# e=list(map(int,input().split()))
# 方法三
# e=[int(i) for i in input().split()]
print("please enter ten integers")
a,b,c,d,e,f,g,h,i,j=map(int,input().split())
s=a+b+c+d+e+f+g+h+i+j
print("sun of ten integers is :",s)
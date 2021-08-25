
a=c=1
b=7
while a<=7:
    while b>=a:
        print(" ",end="")
        b-=1

    while c<=2*a-1:
        print("*",end="")
        c+=1
    a+=1
    b=7
    c=1
    print("")


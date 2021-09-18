# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。

print("please enter ten integers:")

l1=[int(i) for i in input().split()]
print("zui da zhi :",max(l1))
print("zui xiao zhi:",min(l1))
print("ping jun zhi:",sum(l1)/len(l1))
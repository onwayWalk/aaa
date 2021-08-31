'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key


#2、请循环遍历出所有的value


# 3、请在字典中增加一个键值对,"k4":"v4"
'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
for i in dict:
    print(i)
print("-----------------")
for i in dict:
    print(dict[i])
print("-----------------")
dict["k4"]="v4"
for i in dict:
    print(i,dict[i])
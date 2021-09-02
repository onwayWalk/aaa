#
# 中国工商银行开发
# 1.	编程实现：仔细业务之间的包含关系，并完成以下编程需求，要适当提高代码的可复用性。
# a)	用户：账号（str：系统随机产生8位数字）、姓名(str)、密码(int:6位数字)、地址、存款余额(int)、开户行（银行的名称（str））
# b)	地址：国家(str)、省份(str)、街道(str)、门牌号(str)
# c)	银行：能存储100用户的库(可用字典，可用列表)、本银行名称（比如：中国工商银行的昌平支行,str）
# i.	银行业务功能
# 1.	添加用户（传入参数：用户的所有信息。返回值：整型值（1：成功，2：用户已存在，3：用户库已满））
# a)	业务逻辑：
# 	先检查该用户的账号在库里是否存在。若不存在则在用户库里添加一个该用户并返回代号1
# 	若存在则返回代号2。另外在添加用户的时候检测用户库是否已注册满，若已满则返回代号3
# 2.	存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
# a)	业务逻辑：
# 	先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
# 	若有，则将该用户的金额存进去。
# 3.	取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
# a)	业务逻辑：
# 	先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
# 	若存在，则继续判断密码是否正确，若不正确，则返回代号2。
# 	若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
# 	若满足，则将该用户的金额减去。
# 4.	转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
# a)	业务逻辑：
# 	先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
# 	若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
# 	若正确则继续判断要转出的金额是否足够，若不够则返回3，
# 	否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
# 5.	查询账户功能（传入值：账号，账号密码，返回值：空）
# a)	业务逻辑：
# 	先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
# 	否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
# 	若账号和密码都正确，则将该用户的信息都打印出来，比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
# d)	界面类：在执行该入口程序时，就打印银行业务选择菜单：比如：
# i.
# ii.	然后就开始处理各种输入操作，直到业务处理完成!
# 答案：
#
# 开户
import random
bank={}
bank_name='悄悄银行'

def kaihu():
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    address=input('请输入您的地址')
    money=0
    if len(bank)>=100:
        print('你注册的太晚了，我们银行用户已经爆满了')
    elif username in bank:
        print('这个用户已经注册过了')
    else:
        bank[username] = {
            # "account": account,  #
            "password": password,
            'address':address,
            # "country": country,
            # "province": province,
            # "street": street,
            # "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        info='''
                ----------个人信息---------
                       用户名:%s        
                       密码：*****       
                       地址：%s          
                       余额：%s          
                       开户行名称：%s     
                --------------------------
                开户成功
        '''
        print(info%(username,bank[username]['address'],bank[username]['money'],bank_name))
def cunqian():
    while True:
        username=input('请输入用户名:')
        password=input('请输入密码：')
        if username not in bank:
            print('你还没有开户，请先开户')
            break
        else:
            while bank[username]['password']!=password:
                password=input("密码错误,请重新输入密码")
            print('您现在账户%s元' % (bank[username]['money']))
            a=input('请输入存款金额：')
            if a.isdigit():
                bank[username]['money']+=int(a)
                print('尊敬的%s,存钱已完成，您现在账户余额：%s'%(username,bank[username]['money']))
                break
            else:
                print('你输入得什么玩意')
def quqian():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        if username not in bank:
            print('你还没有开户，请先开户')
            break
        else:
            while bank[username]['password'] != password:
                password = input("密码错误,请重新输入密码")

            print('您现在账户%s元'%(bank[username]['money']))
            a=input('请输入取款金额：')
            if a.isdigit():
                if int(a)<= bank[username]['money']:
                    bank[username]['money']-=int(a)
                    print('尊敬的%s,取钱已完成，您现在账户余额：%s'%(username,bank[username]['money']))
                    break
                else :
                    print("你在想屁吃")
            else:
                 print('你输入得什么玩意')


# 定义转账方法
def zhuanzhang():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        if username not in bank:
            print('你还没有开户，请先开户')
            break
        else:
            while bank[username]['password'] != password:
                password = input("密码错误,请重新输入密码")

            gousername=input('请输入要转给的用户名：')
            while gousername not in bank:
                gousername=input('你要转给的用户不存在，请重新输入：')
            if username==gousername:
                print("自己转自己好玩是吧？")
                continue
            print('您现在账户%s元' % (bank[username]['money']))
            gomoney=input('请输入转账金额')
            if gomoney.isdigit():
                if int(gomoney)<= bank[username]['money']:
                    bank[username]['money']-=int(gomoney)
                    bank[gousername]['money'] += int(gomoney)
                    print('尊敬的%s,转账已完成，您现在账户余额：%s'%(username,bank[username]['money']))
                    break
                else :
                    print("你在想屁吃")
            else:
                 print('你输入得什么玩意')
def chaxun():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        while username not in bank:
            username=input('你要查询的用户不存在，请重新输入要查询的用户')

        while bank[username]['password'] != password:
            password = input("密码错误,请重新输入密码")
        info = '''
                ----------个人信息---------
                       用户名:%s        
                       密码：*****       
                       地址：%s          
                       余额：%s          
                       开户行名称：%s     
                --------------------------
                '''
        print(info % (username, bank[username]['address'], bank[username]['money'], bank_name))
while True:
    print('''
    ---------------欢迎来到悄悄银行---------------
    -------------------------------------------
    ----------1.开户            ----------------
    ----------2.存钱            ----------------
    ----------3.取钱            ----------------
    ----------4.转账            ----------------
    ----------5.查询            ----------------
    ----------6.Bye            ----------------
    -------------------------------------------
    ''')
    chose = input('你好，我是你的语音助手悄悄，请输入操作项')
    if chose=='1':
        kaihu()
    elif chose=='2':
        cunqian()
    elif chose=='3':
        quqian()
    elif chose=='4':
        zhuanzhang()
    elif chose=='5':
        chaxun()
    else:
        print('欢迎下次光临')
        break
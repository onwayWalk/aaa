import pymysql


#开户
def kaihu():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='bank', charset='utf8')
    cursor = db.cursor()
    account = input("请输入您的手机号作为您的账号")
    password = input("请输入您的密码")
    name=input("请输入你的姓名")
    address=input('请输入您的地址')
    balance=0
    bankn='悄悄银行'
    sql1="select count(*) from uuser"
    cursor.execute(sql1)
    num=cursor.fetchone()
    sql2="select account from uuser where account=%s"
    cursor.execute(sql2,account)
    res1=cursor.fetchone()

    if num[0]>=100:
        print('你注册的太晚了，我们银行用户已经爆满了')
    elif  res1 :
        print('该手机号已经被注册过了')
    else:
        sql3="insert into uuser value(%s,%s,%s,%s,%s,%s)"

        cursor.execute(sql3,(account,password,name,address,balance,bankn))
        db.commit()

        sql4="select * from uuser where account=%s"
        cursor.execute(sql4,account)

        info =cursor.fetchone()

        info1='''
                ----------个人信息---------
                       账号:%s
                       密码：*****
                       姓名：%s
                       地址：%s
                       余额：%s
                       开户行名称：%s
                --------------------------
                开户成功
        '''
        print(info1%(info[0],info[2],info[3],info[4],info[5]))
        cursor.close()
        db.close()
def cunqian():
    while True:
        db = pymysql.connect(host='localhost', user='root', password='123456', database='bank', charset='utf8')
        cursor = db.cursor()
        account=input('请输入账号:')
        password=input('请输入密码：')
        sql="select account,password,balance from uuser where account=%s"
        cursor.execute(sql,account)
        res1=cursor.fetchone()
        if res1 is None:
            print('该账号还没有开户，请先开户')
            break
        else:
            while res1[1]!=int(password):
                password=input("密码错误,请重新输入密码")
            print('您现在账户%s元'%(res1[2]))
            a=input('请输入存款金额：')
            if a.isdigit():
                sql2="update uuser set balance=%s where account=%s"
                balance=res1[2]+int(a)
                cursor.execute(sql2,(balance,account))
                db.commit()
                sql3="select name,balance from uuser where account=%s"
                cursor.execute(sql3,account)
                res2=cursor.fetchone()

                print('尊敬的%s,存钱已完成，您现在账户余额：%s'%(res2[0],res2[1]))
                break
            else:
                print('你输入得什么玩意')
        db.commit()
        cursor.close()
        db.close()
def quqian():
    while True:
        db = pymysql.connect(host='localhost', user='root', password='123456', database='bank', charset='utf8')
        cursor = db.cursor()
        account=input('请输入账号:')

        sql="select account,password,balance from uuser where account=%s"
        cursor.execute(sql,account)
        res1=cursor.fetchone()
        print(res1)
        if  res1 is None:
            print('该账号还没有开户，请先开户')
            break
        else:
            password = input('请输入密码：')
            while res1[1]!=int(password):
                password=input("密码错误,请重新输入密码")
            print('您现在账户%s元'%(res1[2]))
            b=input('请输入取款金额：')
            if b.isdigit():
                if(res1[2]>int(b)):
                    sql2="update uuser set balance=%s where account=%s"
                    balance=res1[2]-int(b)
                    cursor.execute(sql2,(balance,account))
                    db.commit()
                    sql3="select name,balance from uuser where account=%s"
                    cursor.execute(sql3,account)
                    res2=cursor.fetchone()

                    print('尊敬的%s,取钱已完成，您现在账户余额：%s'%(res2[0],res2[1]))
                    break
                else:
                    print("你个穷鬼账户余额只有%s元，你还想取%s元，你是不是在想屁吃"%(res1[2],b))
            else:
                print('你输入得什么玩意')
        db.commit()
        cursor.close()
        db.close()
def zhuanzhang():
    while True:
        db = pymysql.connect(host='localhost', user='root', password='123456', database='bank', charset='utf8')
        cursor = db.cursor()
        account = input('请输入账号:')

        sql = "select account,password,balance from uuser where account=%s"
        cursor.execute(sql, account)
        res1 = cursor.fetchone()

        if res1:
            password = input('请输入密码：')
            while res1[1] != int(password):
                password = input("密码错误,请重新输入密码")
            print('老板，您现在账户%s元' % (res1[2]))

            goaccount=input('请输入要转给的账号：')
            sql2="select account,balance from uuser where account=%s"
            cursor.execute(sql2,goaccount)
            res2=cursor.fetchone()

            if res2:
                if account==res2[0]:
                    print("自己转自己好玩是吧？是不是脑子秀逗了！")
                    continue
                print('您现在账户%s元' %res1[2])
                gomoney=input('请输入转账金额')
                if gomoney.isdigit():
                    if int(gomoney)<= res1[2]:
                        balance1=res1[2]-int(gomoney)
                        balance2=res2[1]+int(gomoney)
                        sql3="update uuser set balance=%s where account=%s"
                        cursor.execute(sql3,(balance1,res1[0]))
                        cursor.execute(sql3,(balance2,res2[0]))
                        db.commit()
                        sql4="select name,balance from uuser where account=%s"
                        cursor.execute(sql4,account)
                        res3=cursor.fetchone()
                        print('尊敬的%s,转账已完成，您现在账户余额：%s'%(res3[0],res3[1]))
                        break
                    else :
                        print("你个穷鬼账户余额只有%s元，你还想转%s元，你在想屁吃呢！"%(res1[2],gomoney))
                else:
                     print('你输入得什么玩意')
            else:
                print("你要转的账号不存在！")
                break
        else:
            print("你输入的账号不存在，请去开户或者重新输入")
            break
def chaxun():
    while True:
        db = pymysql.connect(host='localhost', user='root', password='123456', database='bank', charset='utf8')
        cursor = db.cursor()
        account = input('请输入要查询的账号:')

        sql1="select * from uuser where account=%s "
        cursor.execute(sql1,account)

        res1=cursor.fetchone()

        if res1:
            password = input('请输入密码：')
            if res1[1]!=int(password):
                print("密码错误!")
                continue
            else:
                info = '''
                                ----------个人信息---------
                                       账号:%s
                                       密码：*****
                                       姓名：%s
                                       地址：%s
                                       余额：%s
                                       开户行名称：%s
                                --------------------------
                        '''
                print(info % (res1[0], res1[2],res1[3],res1[4], res1[5]))
                break
        else:
            print('你要查询的用户不存在!')
            continue
        cursor.close()
        db.close()
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
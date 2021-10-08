from email.mime.text import  MIMEText
from email.header import Header
import smtplib
def connect():
    sender='1430094241@qq.com'
    receiver="1430094241@qq.com"
    senderpass='sqgpbyycectihjec'
    email=MIMEText('python','plain','utf-8')
    email['From']=Header(sender,'utf-8')
    email['To']=Header(receiver,'utf-8')
    email['Subject']=Header('邮件标题','utf-8')

    smtp=smtplib.SMTP_SSL('smtp.qq.com')
    smtp.login(sender,senderpass)
    smtp.connect(host='smtp.qq.com',port=25)
    smtp.sendmail(sender,receiver,email.as_string())
    smtp.quit()


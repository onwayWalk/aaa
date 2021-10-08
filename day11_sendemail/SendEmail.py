
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

mail_host = "smtp.qq.com"  # 设置服务器

sender = '1430094241@qq.com'
mail_pass = "sqgpbyycectihjec"  # 口令
receivers = '1430094241@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

m=MIMEMultipart()
m['From'] = Header(sender)
m['To'] = Header(receivers)
subject = 'Python SMTP 混合邮件测试'
m['Subject'] = subject
message = MIMEText('Python 邮件发送的内容', 'plain', 'utf-8')
m.attach(message)
att1=MIMEText(open('计算机测试报告.html','rb').read(),'base','utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1.add_header('Content-Disposition','attachment',filename="计算机测试报告.html")
# att1["Content-Disposition"] = 'attachment; filename="计算机测试报告.html"'
m.attach(att1)
service=smtplib.SMTP_SSL(mail_host)
service.connect(mail_host,465)
service.login(sender,mail_pass)
service.sendmail(sender,receivers,m.as_string())
print("chengle")
service.quit()

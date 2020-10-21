import smtplib
from email.mime.text import MIMEText                # 导入做纯文本的邮件模板类
from email.mime.multipart import MIMEMultipart      # 导入MIMEMultipart类

# 发邮件相关参数
smtpsever = 'smtp.qq.com'                           # QQ邮箱服务器
sender = '783236348@qq.com'                         # 发送者邮箱
psw = "zaromhkbdwgybfcd"                            # qq邮箱授权码
receiver = '389935145@qq.com'                       # 接收者邮箱账号
port = 465                                          # QQ邮箱服务器默认端口号

# 定义发送邮件的相关参数设置
filepath = r"./readme.txt"                          # 编辑邮件的内容
with open(filepath,'rb') as fp:                     # 读文件
    mail_body = fp.read()

# 主题
msg=MIMEMultipart()
msg["from"] = sender
msg["to"] = receiver
msg["subject"] = "带附件的邮件发送模版主题"

body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"                            # "application/octet-stream" 返回的是二进制文件
att["Content-Disposition"] = 'attachment; filename="test_report.html"'      # test_report.html为重命名附件的名称
msg.attach(att)

# 登录邮箱
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpsever)                           # 连接QQ邮箱服务器
    smtp.login(sender, psw)                           # 调用发件服务
except:
    smtp = smtplib.SMTP_SSL(smtpsever, port)          # 端口错误时执行
    smtp.login(sender, psw)                           # 账号密码错误时执行

smtp.sendmail(sender, receiver, msg.as_string())      # 发送邮件
smtp.quit()
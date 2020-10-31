import os
import smtplib
from email.mime.text import MIMEText            # 邮件模版类
from email.mime.multipart import MIMEMultipart  # 邮件附件类
from email.header import Header                 # 邮件头部模版

class GetMail(object):

    # 发送带邮件的函数动作
    def send_mail(file_new):
        f = open(file_new,'rb')
        mail_body = f.read()
        f.close()

        # 基本信息
        smtpserver = 'smtp.qq.com'      # 邮箱服务器
        pwd = "zaromhkbdwgybfcd"        # 邮箱授权码
        port = 465                      # 邮箱端口

        # 定义邮件主题
        msg=MIMEMultipart()
        msg['subject'] = Header(u'Page Object自动化测试报告','utf-8')
        msg['from'] = "783236348@qq.com"            # 发送者的邮箱
        msg['to'] =  "389935145@qq.com"             # 接收者的邮箱

        # HTML邮件正文 直接发送附件的代码片段
        body=MIMEText(mail_body,"html","utf-8")
        msg.attach(body)
        att = MIMEText(mail_body,"base64","utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)

        # 链接邮箱服务器发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)                    # 连接QQ邮箱服务器
            smtp.login(msg['from'], pwd)                # 调用发件服务
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)   # 端口错误时执行
            smtp.login(msg['from'], pwd)                # 账号密码错误时执行
        # smtp = smtplib.SMTP()
        # smtp.connect(smtpserver)
        # smtp.login(msg['from'],pwd)
        smtp.sendmail(msg['from'], msg['to'], msg.as_string())  # 发送邮件
        # smtp.quit()
        # smtp.sendmail(msg['from'],msg['to'],msg.as_string())
        print ("邮件发送成功")

    #查找最新邮件
    def new_file(test_dir):
        result_dir = test_dir
        lists = os.listdir(result_dir)                      # 列出测试报告目录下面所有的文件
        lists.sort()                                        # 从小到大排序 文件
        file = [x for x in lists if x.endswith('.html')]    # for循环遍历以.html格式的测试报告
        file_path = os.path.join(result_dir,file[-1])       # 找到测试报告目录下面最新的测试报告
        return file_path                                    # 返回最新的测试报告

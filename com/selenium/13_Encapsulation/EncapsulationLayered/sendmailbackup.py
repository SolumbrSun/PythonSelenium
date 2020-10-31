import time
import os
import unittest
import smtplib
from HTMLTestRunner import HTMLTestRunner  #导入生成邮件测试模版
from email.mime.text import MIMEText  #邮件模版类
from email.mime.multipart import MIMEMultipart #邮件附件类
from email.header import Header  #邮件头部模版


# 发送带邮件的函数动作
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    # 基本信息
    smtpserver = 'smtp.qq.com'      # 邮箱服务器
    pwd = "zaromhkbdwgybfcd"        # 邮箱授权码
    port = 465                      # 邮箱端口

    #定义邮件主题
    msg=MIMEMultipart()
    msg['subject'] = Header(u'Page Object自动化测试报告','utf-8')
    msg['from'] = "783236348@qq.com"            # 发送者的邮箱
    msg['to'] =  "389935145@qq.com"             # 接收者的邮箱

    #HTML邮件正文 直接发送附件的代码片段
    body=MIMEText(mail_body,"html","utf-8")
    msg.attach(body)
    att = MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    #链接邮箱服务器发送邮件
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
    lists = os.listdir(result_dir)  #print(lists)  #列出测试报告目录下面所有的文件
    lists.sort()   #从小到大排序 文件
    file = [x for x in lists if x.endswith('.html')]  #for循环遍历以.html格式的测试报告
    file_path = os.path.join(result_dir,file[-1])     #找到测试报告目录下面最新的测试报告
    return file_path  #返回最新的测试报告

if __name__=='__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))  #获取文件所在路径
    test_dir = os.path.join(base_dir,'testcase')  #测试用例所在目录
    test_report = os.path.join(base_dir,'report')  #测试报告所在目录
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'PageObject自动化测试报告',
                            description = u'系统环境:Win10 浏览器:Chrome 用例执行情况:')
    runner.run(testlist)
    fp.close()

    new_report = new_file(test_report)   #获取最新报告文件
    send_mail(new_report)                #发送最新的测试报告
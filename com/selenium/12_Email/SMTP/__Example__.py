import smtplib                                      # 调用smtp发件服务
from email.mime.text import MIMEText                # 导入做纯文本的邮件模板类

smtpsever='smtp.qq.com'                             # QQ邮箱服务器
sender='783236348@qq.com'                           # 发送者邮箱
psw="zaromhkbdwgybfcd"                              # 配置邮箱客户端生成的QQ邮箱授权码
receiver='389935145@qq.com'                         # 接收者邮箱
port=465                                            # QQ邮箱服务器默认端口号
body = '这是一封测试邮件'                             # 邮件的正文内容

msg=MIMEText(body, 'html', 'utf-8')                 # 获取邮件正文内容
msg['from'] = '783236348@qq.com'                    # 发送者账号
msg['to'] = '389935145@qq.com'                      # 接收者账号
msg['subject'] = "这个是纯文本发送的邮件示例"          # 设置邮件主题

smtp = smtplib.SMTP_SSL(smtpsever, port)            # 调用发件服务
smtp.login(sender, psw)                             # 通过发送者的邮箱账号和授权码登录邮箱
smtp.sendmail(sender, receiver, msg.as_string())    # 发送邮件，信息以字符串方式保存
smtp.quit()                                         # 关闭邮件服务
import yagmail

yagindex = yagmail.SMTP(
    user = '783236348@qq.com',          # 发送邮箱
    password = "zaromhkbdwgybfcd",      # 邮箱授权
    host = 'smtp.qq.com'                # 邮箱服务器
)

Yag_contents = ['yagmail发送邮件实例']     # 邮件正文内容
# 接收邮箱,邮件主题，邮件内容
yagindex.send(
    '389935145@qq.com',
    'Yagmail主题',
    Yag_contents
)


# yagindex.send() 可设置多个接收邮箱：yagindex.send(['aa@mail.com', 'bb@mail.com', 'cd@mail.com'], 'subject', 'contents')
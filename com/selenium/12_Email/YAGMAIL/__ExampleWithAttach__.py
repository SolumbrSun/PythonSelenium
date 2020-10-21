import yagmail

yagindex = yagmail.SMTP(
    user = '783236348@qq.com',          # 发送邮箱
    password = "zaromhkbdwgybfcd",      # 邮箱授权
    host = 'smtp.qq.com'                # 邮箱服务器
)
Yag_contents = ['yagmail发送邮件实例']     # 邮件正文内容

# 接收邮箱,邮件主题，邮件内容
yagindex.send(
    ['389935145@qq.com', '783236348@qq.com', 'solumbrsun@gmail.com'],
    'Yagmail主题',
    Yag_contents,
    ['E://Python//SeleniumLearning//com//selenium//12_Email//YAGMAIL//readme.txt',
     'E://Python//SeleniumLearning//com//selenium//12_Email//YAGMAIL//__Example__.py'
     ]
)

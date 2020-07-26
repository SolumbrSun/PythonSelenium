from selenium import webdriver
import time as t
dr = webdriver.Chrome()
dr.get('https://www.jianshu.com/sign_in')
t.sleep(2)
# 点击注册按钮
# 通过ID定位元素，返回的是一个值
js_register = 'document.getElementById("js-sign-up-btn").click();'
dr.execute_script(js_register)
t.sleep(2)

# 点击登录按钮
# js_class = 'document.getElementsByClassName("active")[0].click();'
# dr.execute_script(js_class)
# t.sleep(2)

# 因为跳转到注册页面后，页面元素发生变化，不能再用上方的方法进行定位，改用 find_element_by_xpath() 方法
dr.find_element_by_xpath("//a[@href='/sign_in']").click()

# 输入电话号码或邮箱
js_input = 'document.getElementsByTagName("input")[2].value="17727678721";'
dr.execute_script(js_input)
# 输入密码
js_passwd = 'document.getElementsByTagName("input")[3].value="SolumbrSun";'
dr.execute_script(js_passwd)
t.sleep(2)

# 除了ID定位方法之外，返回的都是一个列表
# js_submit = 'document.getElementsByClassName("sign-in-button")[0].click();'
# dr.execute_script(js_submit)

# JQery是JavaScript的一个库，其中的css选择器常用于元素定位中的策略，使用css选择器定位 登录按钮
# .sign-in-button 表示 class = sign-in-button
css_btn = 'document.querySelectorAll(".sign-in-button")[0].click();'
dr.execute_script(css_btn)
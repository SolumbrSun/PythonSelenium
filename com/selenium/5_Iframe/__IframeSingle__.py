from selenium import webdriver
import time as t
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
t.sleep(2)
# 切换iframe标签
driver.switch_to.frame('login_frame')
driver.find_element_by_name("u").send_keys('783236348@qq.com')
driver.find_element_by_name("p").send_keys('password')
driver.find_element_by_id("login_button").click()
# 退出iframe标签
driver.switch_to.default_content()

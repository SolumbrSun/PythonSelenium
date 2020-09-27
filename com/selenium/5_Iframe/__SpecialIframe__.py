from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
time.sleep(2)
# 使用xpath层级定位iframe标签
# div[2]表示第二个DIV，序列下标从1开始
Xpath=driver.find_element_by_xpath("//div[@class='xm_login_card_cnt']/div[2]/iframe")

# 切换到iframe标签
driver.switch_to.frame(Xpath)
driver.find_element_by_name("u").send_keys('783236348@qq.com')
driver.find_element_by_name("p").send_keys('password')
driver.find_element_by_id("login_button").click()
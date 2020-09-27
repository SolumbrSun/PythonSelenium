from selenium import webdriver
import time as t
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.find_element_by_id("kw").send_keys("渗透吧")
driver.find_element_by_id("su").click()

# 第一个窗口下点击渗透吧链接
# 这里使用的等待的方法，避免页面元素加载过慢而导致出现未找到元素的错误
# driver.implicitly_wait(30)
WebDriverWait(driver,10,2).until(lambda driver: driver.find_element_by_xpath("//*[@id='1']/h3/a"))
driver.find_element_by_xpath("//*[@id='1']/h3/a").click()

# 使用get获取跳转后的url地址
driver.get('https://tieba.baidu.com/f?kw=%C9%F8%CD%B8&fr=ala0&tpl=5')
# t.sleep(3)
# 操作跳转后所在窗口的页面元素
driver.find_element_by_name("kw1").send_keys('大道朝天')
driver.find_element_by_link_text("进入贴吧").click()

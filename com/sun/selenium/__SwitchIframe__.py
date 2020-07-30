from selenium import webdriver
import time as time
driver = webdriver.Chrome()
driver.get('file:///E:/webdriver_api_demo/frame.html')
time.sleep(2)

# 先切换到最外层的iframe标签
driver.switch_to.frame('f1')
# 再切换到第二个iframe标签
driver.switch_to.frame('f2')
# 定位处在第二个iframe标签中的元素
driver.find_element_by_name("email").send_keys('username')
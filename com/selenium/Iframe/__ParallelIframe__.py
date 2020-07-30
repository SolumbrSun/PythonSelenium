# <iframe id='osslog_iframe'></ifame>
# <iframe id='actionFrame'></iframe>

from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get('file:///E:/webdriver_api_demo/frame.html')
t.sleep(2)
# 默认在iframe1标签
driver.switch_to.frame('osslog_iframe')
# 退出iframe1标签
driver.switch_to.default_content()  #退出iframe标签

# 切换到 iframe2标签
driver.switch_to.frame('actionFrame')
# 操作iframe2标签下面的元素
driver.find_element_by_name("email").send_keys('username')
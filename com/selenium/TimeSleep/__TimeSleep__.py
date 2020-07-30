from time import sleep
from selenium import webdriver
# dr = webdriver.Chrome()
# dr.get("https://www.baidu.com")

# 强制等待5s，5s后在执行后面的语句
# sleep(5)
# dr.find_element_by_id('kw').send_keys('双击一下')

# 隐式等待设置 30 s，浏览器不停刷新直到找到目标元素，如果找不到元素就抛出异常，不设置时默认为0
# dr.implicitly_wait(30)
# dr.find_element_by_id('kw').send_keys('双击一下')

# ---------------------------------------------------------------------------------------

# 显示等待：在设置的时间内等到某个元素出现或是某个元素就触发事件，如果超出时长则抛出异常
from selenium import webdriver
from selenium.webdriver.common.by import By   #导入By类
from selenium.webdriver.support.ui import WebDriverWait  #导入WebDriverWait类
from selenium.webdriver.support import expected_conditions as EC  # 导入EC模块

driver = webdriver.Chrome()
driver.get('https://mail.sina.com.cn/')

# WebDriverWait() 表示等待类：driver是驱动，5表示最长超时时间，0.5表示频率
# until()表示停止的条件，返回true停止
# EC.presence_of_element_located(())：每0.5秒执行一次，只要1  冲有一个符合，返回true
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID, 'freename')))
element.send_keys('hello')

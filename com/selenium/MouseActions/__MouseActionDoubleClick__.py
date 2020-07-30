from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  #导入ActionChains类
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
sleep(3)
dr.find_element_by_id('kw').send_keys('双击一下')
#定位百度按钮元素
double = dr.find_element_by_id('su')
#模拟鼠标双击操作
ActionChains(dr).double_click(double).perform()
sleep(5)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #导入ActionChains类
from time import  sleep
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
sleep(3)
#定位百度一下按钮元素
context = dr.find_element_by_id('su')
#鼠标悬停右键操作
ActionChains(dr).context_click(context).perform()
sleep(5)
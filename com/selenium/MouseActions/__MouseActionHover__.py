from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  #导入ActionChains类
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
# 定位到文本内容为【设置】的元素
# find_element_by_link_text() 方法只能对<a></a>标签中的内容起作用
# setting = dr.find_element_by_link_text("设置")
setting = dr.find_element_by_id("s-usersetting-top")
# 鼠标悬停在 【设置】 按钮中
ActionChains(dr).move_to_element(setting).perform()
sleep(1)
# 定位到文本内容为【搜索设置】的元素，并使用 click() 方法触发点击事件
dr.find_element_by_link_text("搜索设置").click()

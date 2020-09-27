from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
# 设置链接
url = "https://www.so.com/"
# get() 获取URL并打开窗口
dr.get(url)
sleep(1)
# 定义文本内容为 360导航 的元素，并点击
dr.find_element_by_link_text("360导航").click()
sleep(2)
# 获取所有窗口的句柄
windows = dr.window_handles
# 通过索引切换到第二个窗口
dr.switch_to.window(windows[1])
sleep(0.5)
# 在第二个窗口里面文本框内输入 第二个窗口
dr.find_element_by_id("search-kw").send_keys("第二个窗口")
sleep(2)
# 切换到第一个窗口
dr.switch_to.window(windows[0])
dr.find_element_by_id("input").send_keys("第一个窗口")

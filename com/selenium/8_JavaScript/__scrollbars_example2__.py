from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys   #引入键盘类
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")  #访问百度搜索
driver.find_element_by_id("kw").send_keys("好奇心日报")
driver.find_element_by_id("su").click()
sleep(5)
#将页面滚动条拖到底部——滚动到定位元素所处位置
driver.find_element_by_xpath('//*[@class="page-inner"]/a[10]').send_keys(Keys.DOWN)
sleep(5)
#将滚动条移动到页面的顶部——滚动到定位元素所处位置
driver.find_element_by_xpath('//*[@id="s_tab"]/div/a[8]').send_keys(Keys.UP)
sleep(5)

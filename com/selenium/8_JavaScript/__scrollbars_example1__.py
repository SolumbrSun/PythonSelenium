from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")  #访问百度搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)
# scrollTo(x,y)——x表示横坐标，y表示纵坐标
driver.execute_script("window.scrollTo(0,10000);") #将页面滚动条拖到底部
sleep(3)
driver.execute_script("window.scrollTo(10000,0);")  #将滚动条移动到页面的顶部
sleep(3)

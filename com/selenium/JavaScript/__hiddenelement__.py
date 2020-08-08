from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
dr = webdriver.Chrome()
dr.get('file:///E:/webdriver_api_demo/frame.html')
sleep(2)
#设置元素为可见
js = 'document.querySelectorAll("select")[0].style.display="block";'
dr.execute_script(js)
sleep(3)
element = dr.find_element(By.ID,"s3")
Select(element).select_by_visible_text("po设计模式") 
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://localhost:8080")
# 定位富文本 并向富文本输入内容 A
js="document.getElementById('content_ifr').contentWindow.document.body.innerHTML='%s'" %('A')
driver.execute_script(js)
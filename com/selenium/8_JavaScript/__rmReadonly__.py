from selenium import webdriver
from time import sleep

def settrain_date(dr):
    train_date = "document.getElementById('train_date').removeAttribute('readonly');"  #移除readonly属性
    dr.execute_script(train_date)
    sleep(2)
    dr.find_element_by_id('train_date').clear()   #清空日期
    dr.find_element_by_id('train_date').send_keys('2018-12-10')  #输入最新日期
    sleep(10)



dr = webdriver.Chrome()
dr.get('https://kyfw.12306.cn/otn/leftTicket/init')
settrain_date(dr)




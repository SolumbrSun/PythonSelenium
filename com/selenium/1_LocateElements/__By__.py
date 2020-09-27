from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element(By.NAME, 'wd').send_keys('solumbrsun')
driver.find_element(By.ID, 'su').click()
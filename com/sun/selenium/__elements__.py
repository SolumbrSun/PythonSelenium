from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# find_elements_by_tag_name（'标签名参数'）：根据括号中定义的标签名进行标签定位
tag = driver.find_elements_by_tag_name('input')
for i in tag:
    # get_attribute('属性名参数') == '属性值参数'： 获取括号中定义的属性名，判断其属性值是否等于条件中的属性值参数——autocomplete的属性值是否等于off
    if i.get_attribute('autocomplete') == 'off':
        # 设置文本内容
        i.send_keys('乘风破浪')
# 根据id名称定位元素，然后通过click()方法进行点击操作
driver.find_element_by_id('su').click()
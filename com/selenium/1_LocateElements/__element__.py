from selenium import  webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 通过find_element_by_id()定位
driver.find_element_by_id("kw").send_keys('大道至简')

# 通过find_element_by_name()定位
driver.find_element_by_name("wd").clear()
driver.find_element_by_name("wd").send_keys('大道朝天')

# 通过find_element_by_class_name()定位
driver.find_element_by_class_name("s_ipt").clear()
driver.find_element_by_class_name("s_ipt").send_keys('斗破苍穹')

# 通过find_element_by_xpath()定位①
# 【//】表示相对路径，【input】表示寻找的元素是个文本输入框，【@id='kw'】表示文本框的id属性值为“kw”
driver.find_element_by_xpath("//input[@id='kw']").clear()
driver.find_element_by_xpath("//input[@id='kw']").send_keys('斗罗大陆')
# 也可用【@name】或【@class】属性
driver.find_element_by_xpath("//input[@name='wd']").clear()
driver.find_element_by_xpath("//input[@name='wd']").send_keys('绝世唐门')
driver.find_element_by_xpath("//input[@class='s_ipt']").clear()
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys('酒神')

# 通过find_element_by_xpath()定位②
# 【//】表示相对路径，【form[@id='form']】表示寻找一个id属性值为“form”的form标签元素，【/】表示下一级标签，
# 【span】表示要在form标签下寻找一个span标签，【input】表示在span标签下寻找一个input标签的元素
# 可将下面的【@id】或【@class】换成其他的属性元素
driver.find_element_by_xpath("//form[@id='form']/span/input[@class='s_ipt']").clear()
driver.find_element_by_xpath("//form[@id='form']/span/input[@class='s_ipt']").send_keys('琴魔')

# 通过find_element_by_xpath()定位③
# 多个标签，加强唯一性
driver.find_element_by_xpath("//input[@class='s_ipt' and @id='kw']").clear()
driver.find_element_by_xpath("//input[@class='s_ipt' and @id='kw']").send_keys('逍遥游')

# 通过find_element_by_css_selector()定位①
# 【id】标签可简写成【#】
driver.find_element_by_css_selector("input#kw").clear()
driver.find_element_by_css_selector("input#kw").send_keys('创世纪')
# 【class】标签可简写成【.】
driver.find_element_by_css_selector("input.s_ipt").clear()
driver.find_element_by_css_selector("input.s_ipt").send_keys('神创纪')

# 通过find_element_by_css_selector()定位②
# 【>】表示标签的层级关系：寻找id属性值为form的便签下的span便签下面input标签且class属性值等于s_ipt的元素
driver.find_element_by_css_selector("form#form>span>input.s_ipt").clear()
driver.find_element_by_css_selector("form#form>span>input.s_ipt").send_keys('魔神传')
# 可用空格替代【>】
driver.find_element_by_css_selector("form#form span input.s_ipt").clear()
driver.find_element_by_css_selector("form#form span input.s_ipt").send_keys('魔神传')



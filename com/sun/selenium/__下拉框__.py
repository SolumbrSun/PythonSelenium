# 下拉框定位要用到 select 类，该类提供三种方式：value， text， index
# <select id = 's4Id'>  == $0
#     <option></option>
#     <option value="01" id="id1">one</option>
#     <option value="02" id="id2">two</option>
#     <option value="03" id="id3">three</option>
# </select>

from selenium import webdriver
from selenium.webdriver.common.by import By             # 导入By类
from selenium.webdriver.support.ui import Select        # 导入 Select类
from time import sleep
dr = webdriver.Chrome()
url = dr.get("网址")
element = dr.find_element(By.ID, "s4Id")

# value 方法，select_by_value("o1") 表示定位到 option value="01" 的选项
Select(element).select_by_value("o1")

# index 方法， select_by_index(1) 表示定位到第二个 option 标签：1表示索引下标。索引位默认从0开始
Select(element).select_by_index(1)

# visible_text属性定位 select_by_visible_text("three"） 表示定位到文本描述为 three 的选项
Select(element).select_by_visible_text("three")


# 元素二次定位: 两次定位操作合并为一步实现
# find_element_by_id("s4Id") 通过 id 定位到 Select 标签
# find_element_by_xpath("//*[@id='id2']") 通过 xpath 定位到 id=id2 的元素
# 二次定位必须添加 click() 方法才会生效
dr.find_element_by_id("s4Id").find_element_by_xpath("//*[@id='id2']").click()
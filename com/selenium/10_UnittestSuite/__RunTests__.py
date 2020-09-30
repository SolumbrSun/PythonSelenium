import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

def getAllCases():
   '''获取tesTcase下面的所有测试模块'''
   Testsuite = unittest.defaultTestLoader.discover(start_dir=os.path.join(os.path.dirname(__file__)), pattern='__TestCases__.py') # pattern为参数名称，从start_dir中获取相关文件
   # os.path.dirname(__file__)——当前文件的绝对路径（不含当前文件名称）；与之相对的是os.path.basename(__file__)——当前文件名称
   return Testsuite

def RunMain():
   '''生成测试报告写入指定Reports目录'''
   fp=open(os.path.join(os.path.dirname(__file__), 'Reports', time.strftime("%Y_%m_%d_%H_%M_%S")+'report.html'),'wb') # wb —— 只写方式打开
   # os.path.join(os.path.dirname(__file__), 'Reports' ——从当前文件中获取绝对路径（不含当前文件名称）后，在获取到的路径下寻找Reports文件夹
   HTMLTestRunner(stream=fp,title='Python+Selenium自动化测试实战',description='基于python语言UI自动化测试').run(getAllCases())

if __name__ == '__main__':
   RunMain()
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

# def getAllCases():
#     '''获取tesTcase下面的所有测试模块'''
#     Testsuite = unittest.defaultTestLoader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'testcase'), pattern='test*.py')
#     # print(os.path.join(os.path.dirname(__file__), 'testcase'))
#     return Testsuite
#
# def RunMain():
#     '''生成测试报告写入指定Reports目录'''
#     fp=open(os.path.join(os.path.dirname(__file__),'report',time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
#     HTMLTestRunner(stream=fp,title='Python+Selenium自动化测试实战', description='基于python语言PO自动化测试').run(getAllCases())
#
# if __name__ == '__main__':
#     RunMain()

class RunTestCases(object):
    def RunMain(base_dir):
        Testsuite = unittest.defaultTestLoader.discover(start_dir=os.path.join(base_dir, 'testcase'), pattern='test*.py')
        fp = open(os.path.join(os.path.dirname(__file__), 'report', time.strftime("%Y_%m_%d_%H_%M_%S") + 'report.html'),'wb')
        HTMLTestRunner(stream=fp, title='Python+Selenium自动化测试实战', description='基于python语言PO自动化测试').run(Testsuite)
        fp.close()
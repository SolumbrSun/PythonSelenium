import os
from EncapsulationLayered.allTests import *
from EncapsulationLayered.sendMail import *

if __name__=='__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    report_dir = os.path.join(base_dir,'report')
    RunTestCases.RunMain(base_dir)               # 执行用例输出报告
    new_report = GetMail.new_file(report_dir)    # 获取最新报告文件
    GetMail.send_mail(new_report)                # 发送最新的测试报告
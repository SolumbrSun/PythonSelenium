# 导入unittes单元测试框架
import unittest

# 测试类默认继承unittest.TestCase
# 测试类下的测试方法必须以test开头
class TestStrSample(unittest.TestCase):
    # 测试运行通过
    def test_split(self):
        s = 'my name is Fighter'
        self.assertEqual(s.split(), ['my', 'name', 'is', 'Fighter'])
    # 用例执行失败，预期结果与实际结果不同
    def test_strendswich(self):
        self.assertEqual('foo'.endswith('o'), False)
    # 用例执行失败，脚本存在错误
    def test_strendswich(self):
        self.assertEqual('foo'.endswth('o'), False)

if __name__ == '__main__':
    # 提供命令行接口，执行test方法后测试结果会记录到测试报告中
    unittest.main()


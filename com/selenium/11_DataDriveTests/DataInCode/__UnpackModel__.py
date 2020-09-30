import ddt
import unittest
Data = [['admin', 'admin', '登录失败'],
        ['admin', 'admin123', '登陆成功'],
        ['', '', '登录失败']]
@ddt.ddt
class TestModules(unittest.TestCase):
    def setUp(self):
        print('testcase beaning....')
    def tearDown(self):
        print('testcase ending.....')

    @ddt.data(*Data)
    @ddt.unpack # 解析列表或元组为多组参数
    def test_DataDriver(self, user, passwd, text):
        print('DDT数据驱动实战演示：', user)
        print('DDT数据驱动实战演示：', passwd)
        print('DDT数据驱动实战演示：', text)

if __name__ == '__main__':
    unittest.main()
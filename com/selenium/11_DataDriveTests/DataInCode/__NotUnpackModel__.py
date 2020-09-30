import ddt
import unittest

Data = [{'name':"keep learing"},
        {'age':18},
        {'address':"深圳地区"},
         'banana']
@ddt.ddt
class TestModules(unittest.TestCase):
    def setUp(self):
        print('testcase beaning....')
    def tearDown(self):
        print('testcase ending.....')

    @ddt.data(*Data) #@ddt.data装饰器可以将参数作为测试数据，参数可以是单个值，列表，元组或字典;根据参数的数量遍历执行
    def test_DataDriver(self, Data):
        print('DDT数据驱动实战演示：', Data)
        # print('DDT数据驱动实战演示：', self)

if __name__ == '__main__':
    unittest.main()
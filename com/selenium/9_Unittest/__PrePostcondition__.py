import unittest

# setUpClass() → setUp() → 第一条测试用例 → tearDown() → setUp() → 第二条测试用例 → tearDown() → tearDownClass()
class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('所有测试用例开始执行前做的操作.....')

    @classmethod
    def tearDownClass(self):
        print('所有测试用例开始执行前做的操作.....')

    def setUp(self):
        print('每条测试用例开始执行前做的操作.....')

    def tearDown(self):
        print('每条测试用例执行完毕后做的操作.....')

    def test_isupper(self):
        self.assertTrue('FOO'.endswith('O'))
        self.assertFalse('Foo'.isupper())
        print('第一条测试用例')
    def test_strendswich(self):
        self.assertEqual('foo'.endswith('o'), True)
        print('第二条测试用例')

if __name__ == '__main__':
    unittest.main()





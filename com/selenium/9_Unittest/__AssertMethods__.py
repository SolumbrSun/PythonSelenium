import unittest
from selenium import webdriver
from time import sleep
class TestWebUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
    def test_QQLogin(self):
        self.driver.get('https://mail.qq.com/cgi-bin/loginpage')
        self.assertEqual(self.driver.title,'登录QQ邮箱', '页面跳转失败，请重新检查！')
    def test_MaoyanMovie(self):
        self.driver.get('https://maoyan.com/')
        self.assertEqual(self.driver.title,'电影院票房购票_评分_选座_经典影视推荐-猫眼电影', '页面跳转失败,请重新检查！')
if __name__ == '__main__':
    unittest.main()

# 常用的断言方法
# assertEqual(first,second,msg=None)	            测试first == second,否则抛出断言异常信息msg
# assertNotEqual(first,second,msg = None)	        测试first!=second,否则抛异常信息msg
# assertTrue(expr,msg=None)	                        测试表达式expr为True，否则抛出断言异常信息msg
# assertFalse(expr,msg=None)	                    测试表达式expr为False，否则抛出断言异常信息msg
# assertIs(a,b,msg=None)	                        测试a和b是同一对象，否则抛出断言异常信息msg
# assertIsNot(a,b,msg=None)	                        测试a和b不是同一对象，否则抛出断言异常信息msg
# assertIsNone(expr,msg=None)	                    测试表达式expr结果为None，否则抛出断言异常信息msg
# assertIsNotNone(expr,msg=None)	                测试表达式expr结果不为None,否则抛出断言信息异常
# assertIn(a,b,msg=None)	                        测试a包含在b中，否则抛出断言异常信息msg
# assertNotIn(a,b,msg=None)	                        测试a不包含在b中，否则抛出断言异常信息msg
# assertIsInstance(obj,cls,msg=None)	            断言obj为cls类型，否则抛出断言异常信息msg.可以用isinstance(obj,cls)或者assertIs(type(obj),cls)代替
# assertNotIsInstance(obj,cls,msg=None)	            断言obj不为cls类型，否则抛出断言异常信息msg.可以用not isinstance(obj,cls)或者assertIsNot(type(obj),cls)代替
# assertRaises(exc[,fun,*args,**kwds])	            测试函数fun(*args,**kwds)抛出exc异常，否则抛出断言异常
# assertRaisesRegexp(exc,r[,fun,*args,**kwds])	    测试函数fun(*args,**kwds)抛出exc异常，同时可以用正则r去匹配异常信息exc，否则抛出断言异常否则抛出断言异常
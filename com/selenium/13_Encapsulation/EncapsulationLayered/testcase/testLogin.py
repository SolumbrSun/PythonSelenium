from EncapsulationLayered.common.ownUnit import *
from EncapsulationLayered.common.helper import *
from EncapsulationLayered.common.getImage import *
from EncapsulationLayered.common.writeLog import *
import unittest

class TestLogin(MyunitTests, Helper, WriteLogs):
    def testlogin(self):
        '''正确的用户名和密码'''
        self.log('PO-gjs：打开浏览器进入到项目首页')
        self.loginpage.openLoginPage()
        self.log('PO-gjs：输入正确用户名和密码')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.log('PO-gjs：登录失败获取信息进行断言')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.log('PO-gjs：登录成功后获取成功信息')
        SaveImage(self.dr,'login_success.png')
        self.log('PO-gjs：第1条用例执行结束.....')

    def testnullpasswd(self):
        '''空密码'''
        self.log('PO-gjs：打开浏览器进入到项目首页')
        self.loginpage.openLoginPage()
        self.log('PO-gjs：输入正确用户名和密码为空')
        self.loginpage.login_gjs_pro(self.readusername(2), self.readpassword(2))
        self.log('PO-gjs：登录失败获取信息进行断言')
        self.assertEqual(self.loginpage.get_passwordNullText(), self.exceptText(2))
        self.log('PO-gjs：登录失败后获取失败信息')
        SaveImage(self.dr,'loginpasswdNull.png')
        self.log('PO-gjs：第2条用例执行结束.....')

    def testnullusername(self):
        '''空用户名'''
        self.log('PO-gjs：打开浏览器进入到项目首页')
        self.loginpage.openLoginPage()
        self.log('PO-gjs：输入空用户名和正确密码')
        self.loginpage.login_gjs_pro(self.readusername(3), self.readpassword(3))
        self.log('PO-gjs：登录失败获取信息进行断言')
        self.assertEqual(self.loginpage.get_userNullText(), self.exceptText(3))
        self.log('PO-gjs：登录失败后获取失败信息')
        SaveImage(self.dr,'loginuserNull.png')
        self.log('PO-gjs：第3条用例执行结束.....')

    def testnulluserandpasswd(self):
        '''空用户名和密码'''
        self.log('PO-gjs：打开浏览器进入到项目首页')
        self.loginpage.openLoginPage()
        self.log('PO-gjs：输入空用户名和空密码')
        self.loginpage.login_gjs_pro(self.readusername(4), self.readpassword(4))
        self.log('PO-gjs：登录失败获取信息进行断言')
        self.assertEqual(self.loginpage.get_userNullText(), self.exceptText(4))
        self.log('PO-gjs：登录失败后获取失败信息')
        SaveImage(self.dr,'loginuserAndpasswd.png')
        self.log('PO-gjs：第4条用例执行结束.....')

if __name__ == '__main__':
    unittest.main(verbosity=2)
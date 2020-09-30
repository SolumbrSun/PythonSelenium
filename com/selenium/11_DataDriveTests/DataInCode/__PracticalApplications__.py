import ddt
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def readData():
    return [['', '', '请输入账号密码'],
            ['admin123@sohu.com', '', '请输入账号密码'],
            ['admin111@sohu.com', '', '请输入账号密码'],
            ['', 'admin123@sohu.com', '请输入账号密码']]

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.testUrl = "https://mail.sohu.com/fe/#/login"

    def tearDown(self):
        self.driver.quit()

    def by_css(self, usernameloc):
        '''重写css定位'''
        return self.driver.find_element_by_css_selector(usernameloc)

    def getassertText(self):
        '''获取验证信息'''
        try:
            sleep(2)
            loctor = (By.CSS_SELECTOR, '.tipHolder.ng-binding')
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位报错！报错原因是：{}'.format(message))

    @ddt.data(*readData())
    @ddt.unpack
    def test_souhuLogin(self, user, passwd, text):
        self.driver.get(self.testUrl)
        sleep(3)
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
        self.by_css('.btn-login.fontFamily').click()
        self.assertEqual(self.getassertText(),text)

if __name__ == '__main__':
    unittest.main()
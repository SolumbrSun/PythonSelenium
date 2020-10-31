from __TestSuite__ import TestWebUI

class TestModle(TestWebUI):
    def test_QQLogin(self):
        self.driver.get('https://mail.qq.com/cgi-bin/loginpage')
        self.assertEqual(self.driver.title,'登录QQ邮箱')
    def test_MaoyanMovie(self):
        self.driver.get('https://maoyan.com/')
        self.assertEqual(self.driver.title,'电影院票房购票_评分_选座_经典影视推荐-猫眼电影')

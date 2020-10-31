from selenium import webdriver
import unittest
from EncapsulationLayered.page.loginPage import *

class MyunitTests(unittest.TestCase):
	def setUp(self):
		self.url = 'https://www.gjfax.com/toLogin'
		self.dr = webdriver.Chrome()
		self.dr.implicitly_wait(30)
		#实例化一个loginpage对象
		self.loginpage = LoginPage(self.url,self.dr)

	def tearDown(self):
		self.dr.quit()

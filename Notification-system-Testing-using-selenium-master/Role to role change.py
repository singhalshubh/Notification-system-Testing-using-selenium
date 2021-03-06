__author__= 'shubh'
import unittest
from decouple import config
from selenium.webdriver.support.select import Select
from selenium import webdriver

class signup(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()

	def login(self,var,driver):
		driver.get(config('url'))
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get(config('url') + 'login/?next=/')
		elem = driver.find_element_by_id("id_username")
		user = config('user').split(',')
		elem.send_keys(user[var])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('pwd'))
		driver.find_element_by_class_name('btn-block').click()

	def fillTheForm(self,driver,var,roleid):
		elem = driver.find_element_by_id("username")
		user = config('user').split(',')
		elem.send_keys(user[var])
		role = config('role').split(',')
		elem = driver.find_element_by_id("role")
		elem.send_keys(role[roleid])
		driver.find_element_by_id('update').click()
		driver.get(config('url') + 'logout/')
		self.login(var,driver)
		driver.get(config('url') + 'notifications/')
		driver.get(config('url') + 'communities/')
		driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/2/"]').click()
		driver.get(config('url') + 'logout/')

	def test_draftToVisisbleState(self):	
		driver = webdriver.Firefox()
		for i in range(1,4):
			for j in range(0,3):
				self.login(0,driver)
				driver.get(config('url') + 'communities/')
				driver.find_element_by_xpath('//a [@href="/community-view/2/"]').click()
				driver.find_element_by_xpath('//a [@href="/manage_community/2/"]').click()
				self.fillTheForm(driver,i,j)
		
			
			
	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()
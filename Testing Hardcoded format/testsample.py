__author__= 'shubh'
import unittest
from selenium import webdriver

class signup(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.user = "shubh"
		self.pwd = "sha123#56su"
		self.url = "http://127.0.0.1:8000/"

	def test_draftToVisisbleState(self):
		driver = webdriver.Firefox()
		driver.get(self.url)
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get(self.url + 'login/?next=/')
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(self.user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(self.pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get(self.url + 'mydashboard/')
		driver.find_element_by_xpath('//a [@href="/article-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/1/"]').click()
		#make the id as visible of the button of visible in html file
		driver.find_element_by_id('visible').click()
		driver.find_element_by_xpath('//a [@href="/community-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/1/"]').click()

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
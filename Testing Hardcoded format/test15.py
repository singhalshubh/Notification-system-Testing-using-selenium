__author__= 'shubh'
import unittest
from selenium import webdriver

class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def draftToVisisbleState(self):
		user ="shubh"
		pwd= "sha123#56su"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a [@href="/mydashboard/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-view/3 /"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/3 /"]').click()
		#make the id as visible of the button of visible in html file
        driver.find_element_by_id('visible').click()
        driver.find_element_by_xpath('//a [@href="/community-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/group-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/group-feed/1/"]').click()

	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
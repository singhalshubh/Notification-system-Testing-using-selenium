__author__= 'shubh'
import unittest
from selenium import webdriver

class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def draftToVisisbleState(self):
		user ="raghav"
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
		driver.find_element_by_xpath('//a [@href="/communities/"]').click()
        driver.find_element_by_xpath('//a [@href="/community-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/group-view/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/group_content/1/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-view/4/"]').click()
		driver.find_element_by_xpath('//a [@href="/article-edit/4/"]').click()
		#save article class
		driver.find_element_by_class_name('save_article').click()
		driver.find_element_by_xpath('//a [@href="/logout/"]').click()
		user ="ty"
		pwd= "sha123#56su"
		driver.get("http://localhost:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a [@href="/notifications/"]').click()


	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
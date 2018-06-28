__author__= 'shubh'
import unittest
from selenium import webdriver

class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_unsubscribe_community(self):
		user ="shubh"
		pwd= "sha123#56su"
		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://127.0.0.1:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a [@href="/communities/"]').click()
		driver.find_element_by_xpath('//a [@href="/community-view/1/"]').click()
		driver.find_element_by_id("Unsubscribe").click()
		driver.find_element_by_id("Yes").click()
		driver.find_element_by_xpath('//a [@href="/logout/"]').click()
		user ="ty"
		pwd= "sha123#56su"
		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://127.0.0.1:8000/")
		driver.find_element_by_xpath('//a [@href="/login/?next=/"]').click()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_xpath('//a [@href="/community_feed/1/"]').click()

	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
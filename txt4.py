import unittest
from selenium import webdriver


import time



class MasterRecipesTest(unittest.TestCase):
	username = 'A.Rabia'
	first_name = 'Rabia'
	email = 'annakachan1@gmail.com'
	password = 'lizka88'
	

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get('https://www.master-recipes.com/')

	def test_registration(self):
		self.driver.find_element_by_xpath("//div[@class='reg']").click()
		self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
		self.driver.find_element_by_xpath("//input[@name='first_name']").send_keys(self.first_name)
		self.driver.find_element_by_xpath("//input[@type='email']").send_keys(self.email)
		self.driver.find_element_by_xpath("//input[@placeholder='Пароль:']").send_keys(self.password)
		self.driver.find_element_by_xpath("//input[@name='submit']").click()

	def tearDown(self):
		self.driver.quit()



if __name__ == '__main__':

	unittest.main()

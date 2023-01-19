import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner

class OrangeHtmlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('/Users/vaibhavlutade/PycharmProjects/mnewproject/driver/chromedriver 2')

    def test_HomePage(self):
        self.driver.get("https://staging-cu.reposenergy.com/auth/login")
       # self.assertEqual('Google',self.driver.titile,"not matched")
       # time.sleep(5)

    def test_Login(self):
        self.driver.get("https://staging-cu.reposenergy.com/auth/login")
        self.driver.find_element(By.XPATH, "//*[@id='Email address / mobile ']").send_keys("9008641259")
        self.driver.find_element(By.NAME, "password").send_keys("repos1234")
        self.driver.find_element(By.XPATH, "//*[@id='sign-in-btn']/span[1]").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='//Users//vaibhavlutade//PycharmProjects//mnewproject//seleniumpackage//Reports'))





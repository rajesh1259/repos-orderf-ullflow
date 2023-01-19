from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
class myurl_Test(unittest.TestCase):
    @pytest.fixture()
    def setup(self):
        global driver
        self.driver=webdriver.chrome('/Users/vaibhavlutade/PycharmProjects/mnewproject/driver/chromedriver 2')
        yield
        self.driver.close()

    def test_homepagetitle(self,setup):
        self.driver.get("https://staging-cu.reposenergy.com/auth/login")

    def test_login(self,setup):
        self.driver.get("https://staging-cu.reposenergy.com/auth/login")
        self.driver.find_element(By.NAME, "inputName").send_keys("9008641259")
        self.driver.find_element(By.NAME, "password").send_keys("repos1234")
        self.driver.find_element(By.XPATH, "//*[@id='sign-in-btn']/span[1]").click()

#testbb=myurl_Test()
#testbb.test_homepagetitle()
#testbb.test_login()




if __name__=='__main__':
    unittest.main












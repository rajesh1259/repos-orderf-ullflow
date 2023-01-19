import pytest
import unittest
from selenium import webdriver
import sys
import path
import sys.path.append("/Users/vaibhavlutade/PycharmProjects/mnewproject")
from pagobjm.TestLogin import testLogin

class logintest(unittest.TestCase):
    baseurl="https://staging-cu.reposenergy.com/auth/login"
    usernameid="9008641259"
    passwordpass="repos1234"
    driver1=webdriver.Chrome('/Users/vaibhavlutade/PycharmProjects/mnewproject/driver/chromedriver 2')

    def test_finallogin(self):
        self.driver.get(baseurl)
        xrt=testLogin(self.driver1)
        xrt.test_username(self.usernameid)
        xrt.test_password(self.passwordpass)


if __name__=='__main__':
    unittest.main








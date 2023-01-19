import unittest
import tracemalloc
from selenium import webdriver

'''from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time'''

class Test(unittest.TestCase):
    def testName(self):
        # driver=webdriver.Chrome('../driver/chromedriver 2')
        # driver.get("https://www.google.com/")
        # test = driver.title
        # #self.assertEqual("Google45",test,"title is not same")
        # #self.assertNotEqual("Google",test,"title is not same")
        # #self.assertTrue("Google",test)
        # self.assertIsNone(driver)
          mylist=["python","java","selenium"]
          self.assertIn("java",mylist)

tracemalloc.start()

'''if __name__ == "__main__":
    unittest.main'''
test4=Test()
test4.testName()







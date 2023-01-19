from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"name").send_keys("baner")
driver.find_element(By.ID,"confirmbtn").click()
test=driver.switch_to.alert
time.sleep(2)
test.dismiss()
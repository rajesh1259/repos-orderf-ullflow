import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
opennewwindow=driver.window_handles
driver.switch_to.window(opennewwindow[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(opennewwindow[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

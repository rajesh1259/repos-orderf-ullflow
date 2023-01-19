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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,800);")
#driver.maximize_window()
time.sleep(5)
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Job Support").click()
driver.execute_script("window.scrollBy(0,800);")
#print(driver.find_element(By.TAG_NAME,"h1").text)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//button[text()='Home']").click()
time.sleep(2)
driver.get_screenshot_as_file("pintes.png")


#driver.execute_script("window.scrollBy(0,800);")

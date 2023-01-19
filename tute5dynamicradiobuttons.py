from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radios=driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio in radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        break
driver.close()


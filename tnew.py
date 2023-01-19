from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('../driver/chromedriver')

driver.get("https://www.facebook.com/login/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element(By.ID, "email").send_keys("rajeshsomawanshi@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("Facebook@1259")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.title)


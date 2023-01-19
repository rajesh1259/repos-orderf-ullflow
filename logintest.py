import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(10)
driver.get("https://staging-cu.reposenergy.com/overview")
driver.find_element(By.NAME, "inputName").send_keys("98328")
driver.find_element(By.NAME, "password").send_keys("r1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
time.sleep(5)
data=driver.switch_to.alert
student=data.text
time.sleep(2)
print(student)

data.accept()
time.sleep(5)
data.accept()
time.sleep(2)
assert "In-valid E-mail, please correct and try again!".is_displayed()

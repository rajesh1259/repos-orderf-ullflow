from telnetlib import EC

import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://staging-pa.reposenergy.com/login")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("8221133445")
driver.find_element(By.NAME,"password").send_keys("repos1234")
driver.find_element(By.XPATH,"//span[text()='Log In']").click()
time.sleep(10)
element=driver.title
print(element)

#postive test case: use logged in sucessfully
assert element == 'Login'
# time.sleep(5)
#assert driver.find_element(By.XPATH,"//span[text()='Update']").is_displayed()
# wait=WebDriverWait(driver,10)
# wait.until(EC.url_changes("https://stagi443ng-pa.reposenergy.com/app/finserv4444"))

#driver.close()
# assert driver.find_element(By.ID,"client-snackbar").is_displayed()
# print(driver.find_element(By.ID,"client-snack").text)


#assert driver.find_element(By.XPATH,"//span[text()='Overview']").is_displayed()

#print(driver.title)

#negative test case:by entering invalide  username and valid password
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://staging-pa.reposenergy.com/login")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("822113gg5")
driver.find_element(By.NAME,"password").send_keys("repos1234")

driver.find_element(By.XPATH,"//span[text()='Log In']").click()
time.sleep(5)

assert driver.find_element(By.ID,"client-snackbar").is_displayed()
print(driver.find_element(By.ID,"client-snackbar").text)

time.sleep(5)






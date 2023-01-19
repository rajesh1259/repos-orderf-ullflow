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
driver.find_element(By.NAME, "inputName").send_keys("4444444147")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//ul/li[4]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@href='/assets/create']").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/input[1]").click()
time.sleep(5)
text=driver.find_element(By.ID,"searchTextField")
text.clear()
time.sleep(10)
#text.send_keys("ashok nagar, pune")
time.sleep(10)
#driver.find_element(By.ID,"asset-name").send_keys("sinchan nagar")
driver.find_element(By.NAME,"pinCode").send_keys("585416")
driver.find_element(By.XPATH,"//span[text()='200 L']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Create Asset']").click()
time.sleep(5)
'''element=driver.find_elements(By.XPATH,"//div/ul/li")
for i in element:
    if i.text=="Orders":
        i.click()
        break'''

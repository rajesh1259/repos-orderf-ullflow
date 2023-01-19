import driver as driver
import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(5)
driver.get("https://staging-cu.reposenergy.com/overview")
driver.find_element(By.NAME, "inputName").send_keys("9823521834")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
#time.sleep(5)
driver.maximize_window()
#time.sleep(5)
driver.find_element(By.ID,"Ongoing Orders reroute").click()
driver.find_element(By.ID,"additional-actions1-header").click()
driver.find_element(By.XPATH,"//span[text()='Track Order']").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH,"//span[text()='Cancel']").click()

driver.find_element(By.XPATH,"//span[text()='Cancel Order']").click()

driver.close()
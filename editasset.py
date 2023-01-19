import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(5)
driver.get("https://staging-cu.reposenergy.com/overview")
driver.find_element(By.NAME, "inputName").send_keys("9823521834")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
driver.maximize_window()
#time.sleep(5)
driver.find_element(By.XPATH,"//ul/li[4]").click()
driver.find_element(By.XPATH,"//span[text()='Sub-Assets']").click()
driver.find_element(By.XPATH,"//span[text()='Add Sub-Asset']").click()
driver.find_element(By.NAME,"name").send_keys("mh99111")
driver.find_element(By.NAME,"mobile").send_keys("7788665576")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Cars']"))).click()
driver.find_element(By.XPATH,"//span[text()='Create Sub-Asset']").click()


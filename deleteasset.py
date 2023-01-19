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
driver.find_element(By.NAME, "inputName").send_keys("4444444147")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//ul/li[4]").click()
time.sleep(5)

#code for delete asset
'''driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/main[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/button[1]/span[1]/*[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//h5[text()='Balewadi Asset']")
driver.find_element(By.XPATH,"//span[text()='Yes Delete']").click()
time.sleep(5)'''

#code for update asset

driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-0']/div/p/div/div[2]/div[1]/div/div[2]/div[3]/div/div[3]/div/a[2]").click()
time.sleep(5)
driver.find_element(By.NAME,"name").send_keys([Keys.BACKSPACE] * 20)
pyautogui.typewrite('Pashan')
time.sleep(5)
driver.find_element(By.ID,"searchTextField").send_keys([Keys.BACKSPACE] * 80)
pyautogui.typewrite('pashan,pune')
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Modify Asset']").click()
time.sleep(5)
driver.close()
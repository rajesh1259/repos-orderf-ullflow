import driver as driver
import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
driver.find_element(By.XPATH,"//ul/li[5]").click()
time.sleep(5)
'''driver.find_element(By.NAME,"phone").send_keys([Keys.BACKSPACE] * 10)
pyautogui.typewrite('4444444147')
time.sleep(5)
driver.find_element(By.NAME,"phone").send_keys(Keys.DELETE)
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys([Keys.BACKSPACE] * 16)
pyautogui.typewrite('test22222@gmail.com')
driver.find_element(By.ID,"submit-btn").click()'''

#code for report issue

'''driver.find_element(By.XPATH,"//span[text()='Report an Issue']").click()
driver.find_element(By.NAME,"subject").send_keys("dashboard testing issue")
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/main/div[1]/div[3]/div/div[1]/div[2]/form/div/div[2]/div/div/input").send_keys("some buttons are not working")
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,"description"))).click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Submit']").click()'''
driver.close()


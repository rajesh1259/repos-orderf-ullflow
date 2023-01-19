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
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//ul/li[4]").click()
time.sleep(5)

#code for refill report

# driver.find_element(By.XPATH,"//a[@href='/assets/dispense/6553/Ashok Nagar Asset n4/8']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-0']/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/button").click()
# driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/button[1]/span[1]").click()
# elements=driver.find_elements(By.XPATH,"//div/div[7]/button/span/p[@class='MuiTypography-root MuiTypography-body2 "
#                                        "MuiTypography-colorInherit']")
# time.sleep(5)
# for i in elements:
#     if i.text=='31':
#         i.click()
#         break
# time.sleep(5)
# driver.find_element(By.XPATH,"//span[text()='OK']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-0']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/button/span[1]").click()
# dataitems=driver.find_elements(By.XPATH,"//div/div[1]/button/span/p[@class='MuiTypography-root MuiTypography-body2 MuiTypography-colorInherit']")
# time.sleep(5)
# for item in dataitems:
#     if item.text=='1':
#         item.click()
#         break
# time.sleep(5)
# driver.find_element(By.XPATH,"//span[text()='OK']").click()


#CODE FOR DISPENSE REPORT

driver.find_element(By.XPATH,"//a[@href='/assets/dispense/6097/Datum Test/1']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Dispense']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-1']/div/div[1]/div[1]/div[2]/div/div["
                             "1]/div/div/div/button/span[1]").click()

driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/button[1]/span[1]").click()

time.sleep(5)
testss=driver.find_elements(By.XPATH,"//div/div[7]/button/span/p[@class='MuiTypography-root MuiTypography-body2 "
                                     "MuiTypography-colorInherit']")
time.sleep(5)
for data in testss:
    if data.text=='10':
        data.click()
        break
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='OK']").click()
driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-1']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div/button/span[1]").click()
time.sleep(5)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/button[1]/span[1]").click()
time.sleep(5)
tents=driver.find_elements(By.XPATH,"//div/div[1]/button/span/p[@class='MuiTypography-root MuiTypography-body2 MuiTypography-colorInherit']")
time.sleep(5)
for ten in tents:
    if ten.text=='11':
        ten.click()
        break
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='OK']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-1']/div/div[1]/div[1]/div[2]/div/div[3]/button/span[1]").click()
time.sleep(5)

driver.close()
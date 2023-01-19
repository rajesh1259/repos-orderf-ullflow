from selenium.common.exceptions import TimeoutException


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from hashlib import new
from select import select

import driver as driver
import of as of
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('../driver/chromedriver')
#driver.implicitly_wait(5)
driver.get("https://finserv-sa.reposenergy.com/sign-in")
driver.maximize_window()
#driver.maximize_window()
driver.find_element(By.NAME, "userName").send_keys("7024069945")
driver.find_element(By.NAME, "password").send_keys("7024069945")
driver.find_element(By.XPATH, "//span[text()='Sign in now']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()=' RPP Orders']").click()
time.sleep(10)
#element=driver.find_element(By.XPATH,"//tbody/tr[2]/td/span[@class='MuiButtonBase-root MuiIconButton-root jss929 MuiCheckbox-root MuiCheckbox-colorPrimary MuiIconButton-colorPrimary']")
##driver.find_element(By.XPATH,"//span[@class='MuiButtonBase-root MuiIconButton-root jss221 MuiCheckbox-root MuiCheckbox-colorSecondary MuiIconButton-colorSecondary']").click()
#element=driver.find_element(By.ID, "7515")

#element=driver.find_element(By.ID,"update-status-outlined-label")

    # drop=Select(element)
driver.find_element(By.ID,"search_input").send_keys("test108")
time.sleep(15)

driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span").click()
time.sleep(10)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Change Order Status']"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Delivered']"))).click()
driver.find_element(By.ID,"outlined-size-small").send_keys("200")
driver.find_element(By.XPATH,"//span[text()='Update']").click()




    # //option[text()='Change Order Status']



'''element=driver.find_element(By.ID,"update-status-outlined-label")
drop=select(element)
drop.select_by_index(1)'''
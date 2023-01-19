
import self as self
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('../driver/chromedriver')

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()
# driver.find_element(By.NAME, "inputName").send_keys("9834810128")
# driver.find_element(By.NAME, "password").send_keys("repos1234")
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
# time.sleep(10)
# #driver.find_element(By.XPATH,"//ul/li[3]").click()
# driver.find_element(By.XPATH,"//*[@id='place-order-btn']/span[1]").click()
# #driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
'''element = driver.find_element(By.ID, "continents")
drop=Select(element)
drop.select_by_index(2)'''
#dropdown=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]/select[1]"))
#dropdown.select_by_index(56)










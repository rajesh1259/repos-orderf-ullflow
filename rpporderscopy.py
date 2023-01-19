import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://finserv-sa.reposenergy.com/sign-in")
driver.maximize_window()
#driver.maximize_window()
driver.find_element(By.NAME, "userName").send_keys("7024069945")
driver.find_element(By.NAME, "password").send_keys("7024069945")
driver.find_element(By.XPATH, "//span[text()='Sign in now']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()=' RPP Orders']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span").click()
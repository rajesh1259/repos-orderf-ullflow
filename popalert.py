from selenium import webdriver

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://staging-cu.reposenergy.com/auth/login")
driver.find_element(By.NAME,"inputName").send_keys("9008641259")
driver.find_element(By.ID,"Password").send_keys("repos12345")
driver.find_element(By.XPATH,"//*[@id='sign-in-btn']/span[1]").click()
driver.maximize_window()
time.sleep(5)
#driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()



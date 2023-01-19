from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
#driver.switch_to.frame(1)
#driver.switch_to.frame(0)
vert = driver.find_element(By.NAME,"userfile").send_keys("/Users/vaibhavlutade/Desktop/upload.png")
driver.find_element(By.XPATH,"/html/body/form/input[2]").click()
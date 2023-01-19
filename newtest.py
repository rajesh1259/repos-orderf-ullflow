from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time
'''email = "rajeshsomawanshi@gmail.com"
password = "Facebook@1259"'''


driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://www.facebook.com/login/")
time.sleep(5)
driver.maximize_window()
driver.get("https://staging-cu.reposenergy.com")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
'''username_textbox = driver.find_element(By.ID, "email")
username_textbox.send_keys(email)
password_textbox = driver.find_element(By.NAME, "pass")
password_textbox.send_keys(password)
login_button = driver.find_element(By.ID, "loginbutton")
login_button.click()'''
'''driver.close()
login_button = driver.find_element(By.ID, "sign-in-btn")
login_button.click()
driver.maximize_window()
time.sleep(30)
asset_tab = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/nav/div/ul/li[3]/div/a/span[1]/text()")
asset_tab.click()
addasset_button = driver.find_element(By.XPATH,"")
addasset_button.click()'''

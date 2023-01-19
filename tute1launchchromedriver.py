from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('../driver/chromedriver')

driver.get("https://staging-cu.reposenergy.com/overview")
'''print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element(By.NAME, "inputName").send_keys("9834810128")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()'''

driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot Password?").click()
driver.find_element(By.NAME,"mobile").send_keys("9834810128")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
driver.get("https://staging.reposenergy.com/api/web/v1/customer/user_reset_password?key=98348101284M57YTD0DVW0VQE8NFH9KA12HQ8GTITE8JEF0QC9UHNSMQ8TVPK8E2MLLIJ0A")
driver.find_element(By.ID,"password").send_keys("veer1234")
driver.find_element(By.ID,"confirm_password").send_keys("veer1234")
driver.find_element(By.XPATH,"//input[@type='submit']").click()



from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('../driver/chromedriver')

driver.get("https://staging-cu.reposenergy.com/overview")
driver.implicitly_wait(10)



driver.find_element(By.NAME, "inputName").send_keys("9008641259")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "//*[@id='sign-in-btn']/span[1]").click()

'''assert "Good Morning, Rajesh somvanshi" in driver.title'''


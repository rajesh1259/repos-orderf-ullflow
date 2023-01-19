from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('../driver/chromedriver')
'''driver.get("https://chercher.tech/python/install-try-xpath-selenium-python")
driver.find_element(By.LINK_TEXT,"CSS Selector").click()
driver.find_element(By.LINK_TEXT,"Css Selector in Selenium python").click()
driver.find_element(By.LINK_TEXT,"Wild card in CSS selector").click()'''

#from selenium import webdriver

# create webdriver object


# get geeksforgeeks.org
driver.get("https://www.tutorialspoint.com/index.htm")

# get current_window_handle
test = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div/div[1]/a/p/b")
driver.execute_script("arguments[0].scrollIntoView();",test)


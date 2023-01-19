import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(5)
#listo=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(4)
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
'''oldlist=driver.find_elements(By.XPATH,"//tr/td[1]")
for i in oldlist:
    listo.append(i.text)
listn=listo.copy()
listo.sort()
assert listn==listn'''
elements=driver.find_elements(By.XPATH,"//tr/td[3]")
for i in elements:
    print(i.text)
import self as self
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#print(countries)
time.sleep(2)

'''for country in countries:
    if country.get_attribute("value") == "India":
        country.click()
        break'''

for i in countries:
    if i.text=="India":
        i.click()
        break

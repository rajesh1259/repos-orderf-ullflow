import self as self
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
'''element = driver.find_element(By.ID, "continents")
drop=Select(element)
drop.select_by_index(2)

#drop.select_by_visible_text("Europe")'''
test = driver.find_element(By.ID,"continents")
newtest = Select(test)
newtest.select_by_index(2)




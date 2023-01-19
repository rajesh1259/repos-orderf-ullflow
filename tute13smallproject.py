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
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Shop']").click()
time.sleep(5)
'''elements=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
time.sleep(5)
for i in elements:
    newele=i.find_element(By.XPATH,"div/h4/a").text
    #print(newele)
    if newele == "Samsung Note 8":
        i.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

for i in elements:
    textname=i.find_element(By.XPATH,"div/h4/a").text
    #print(textname.text)
    if textname == "Nokia Edge":
        i.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()'''
driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[1]/div[1]/div[2]/button[1]").click()









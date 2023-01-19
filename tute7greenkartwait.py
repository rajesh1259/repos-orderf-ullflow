#import By as By
import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for i in results:
    print(i.text)
#print(len("results"))
for result in results:
    result.find_element(By.XPATH,"div/button").click()
#time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
#time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
#wait=WebDriverWait(driver,15)
#wait.until(expected_conditions.presence_of_element_located(By.XPATH,"//input[@type='text']")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
#time.sleep(1)
obtxt=driver.find_element(By.XPATH,"//span[text()='Code applied ..!']").text
print(obtxt)
time.sleep(15)
test2=driver.find_elements(By.XPATH,"//tbody/tr/td[5]")
#print(len(test2))
sum=0
for tests in test2:
    sum=sum + int(tests.text)
#print(sum)
test3=int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
#print(test3)
assert sum==test3


#driver.find_element(By.XPATH,"//button[text()='Place Order']").click()'''
#time.sleep(2)

driver.close()





from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
driver = webdriver.Chrome('../driver/chromedriver')
driver.get("https://www.orangehrm.com/open-source/demo/")
driver.maximize_window()
main = driver.find_element(By.XPATH,"//*[@id='header-navbar']/ul[1]/li[4]/a")
subm = driver.find_element(By.XPATH,"//*[@id='header-navbar']/ul[1]/li[4]/ul/div/div/div/p[1]/a")
act=ActionChains(driver)
act.move_to_element(main).move_to_element(subm).click().perform()
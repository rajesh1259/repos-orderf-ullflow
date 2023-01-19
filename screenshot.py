from selenium import webdriver
driver = webdriver.Chrome('../driver/chromedriver')

driver.get("https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/")
#driver.save_screenshot("/Users/vaibhavlutade/Desktop/myscreen.png")
driver.get_screenshot_as_file("/Users/vaibhavlutade/Desktop/myscreen1.png")
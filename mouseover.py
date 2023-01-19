from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

driver = webdriver.Chrome('../driver/chromedriver')
'''driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//*[@id='topNavData']/li[1]/div/a")
element = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
actions= ActionChains(driver)
actions.double_click(element).perform()
driver.get("https://staging-sa.reposenergy.com/sign-in")
driver.find_element(By.NAME,"userName").send_keys("7024069945")
driver.find_element(By.NAME,"password").send_keys("7024069945")
driver.find_element(By.XPATH,"//*[@id='login']/span[1]").click()
elementn = driver.find_element(By.CSS_SELECTOR,"div.MuiDrawer-root.MuiDrawer-modal:nth-child(5) div.MuiPaper-root.MuiDrawer-paper.jss857.MuiDrawer-paperAnchorLeft.MuiPaper-elevation16:nth-child(3) nav.jss984.jss858 div.MuiList-root:nth-child(5) a.MuiListItem-root.jss995.MuiListItem-gutters:nth-child(3) div.MuiListItemText-root > span.MuiTypography-root.MuiListItemText-primary.jss998.MuiTypography-body1.MuiTypography-displayBlock")
action= ActionChains(driver)
action.context_click(elementn).perform()'''
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
selement =driver.find_element(By.ID,"box7")
delement =driver.find_element(By.ID,"box106")
actions= ActionChains(driver)
actions.drag_and_drop(selement,delement).perform()





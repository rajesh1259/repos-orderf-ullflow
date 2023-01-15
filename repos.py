import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('../driver/chromedriver')
driver.implicitly_wait(5)
driver.get("https://staging-cu.reposenergy.com/overview")
driver.find_element(By.NAME, "inputName").send_keys("4444444147")
driver.find_element(By.NAME, "password").send_keys("repos1234")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//ul/li[3]").click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,"#place-order-btn").click()
driver.find_element(By.XPATH,"//span[text()='200 L']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='radio']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//span[text()='Place Order']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Continue']").click()
time.sleep(4)
#driver.find_element(By.XPATH,"//span[text()='NEFT/RTGS']").click()
time.sleep(10)
#parnet app flow starts
driver.get("https://staging-pa.reposenergy.com/login")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("8221133445")
driver.find_element(By.NAME,"password").send_keys("repos1234")
driver.find_element(By.XPATH,"//span[text()='Log In']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Orders']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Accept']").click()
time.sleep(5)

driver.get("https://finserv-sa.reposenergy.com/sign-in")
driver.maximize_window()
#driver.maximize_window()
driver.find_element(By.NAME, "userName").send_keys("7024069945")
driver.find_element(By.NAME, "password").send_keys("7024069945")
driver.find_element(By.XPATH, "//span[text()='Sign in now']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()=' RPP Orders']").click()
time.sleep(10)

driver.find_element(By.ID,"search_input").send_keys("test108")
time.sleep(25)

driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span").click()
time.sleep(10)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Change Order Status']"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Delivered']"))).click()
driver.find_element(By.ID,"outlined-size-small").send_keys("200")
driver.find_element(By.XPATH,"//span[text()='Update']").click()







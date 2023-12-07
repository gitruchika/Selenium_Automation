from selenium import webdriver
from test_data import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(timeout)
# alert box
# driver.find_element(By.ID, "btnShowMsg").click()
# time.sleep(3)
# alert_obj = Alert(driver)
# print(alert_obj.text)
# alert_obj.accept()

# --- Confirm Box -----
# driver.find_element(By.ID, "button").click()
# time.sleep(3)
# alert_obj = Alert(driver)
# alert_obj.accept()
# ui_msg = driver.find_element(By.ID, "demo").text
# assert ui_msg == ok_msg

# alert_obj.dismiss()
# ui_msg = driver.find_element(By.ID, "demo").text
# assert ui_msg == cancel_msg

### --

driver.find_element(By.ID, "promptbtn").click()
time.sleep(3)
alert_prompt = Alert(driver)
alert_prompt.send_keys("SQATools")
time.sleep(3)

alert_prompt.accept()

time.sleep(5)
driver.close()






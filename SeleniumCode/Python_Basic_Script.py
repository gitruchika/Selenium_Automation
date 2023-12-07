from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://google.co.in")
# driver.find_element(By.NAME, "q").send_keys("Python Programming")
# driver.find_element(By.ID, "APjFqb").send_keys("Python Programming")
# driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Python Programming")
# driver.find_element(By.TAG_NAME, "textarea").send_keys("Python Programming")
# driver.find_element(By.NAME, "btnK").click()
# driver.find_element(By.LINK_TEXT, "Gmail").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Gma").click()
time.sleep(5)
driver.close()


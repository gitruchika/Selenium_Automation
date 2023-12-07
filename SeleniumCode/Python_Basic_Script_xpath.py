from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
assert driver.find_element(By.XPATH, "//img[@alt='Facebook']")
driver.find_element(By.XPATH, "//input[@data-testid='royal_email']").send_keys("testuser@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Testadmin@123")
driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']").click()

time.sleep(5)
driver.close()


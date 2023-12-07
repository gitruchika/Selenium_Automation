from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.get('https://automationbysqatools.blogspot.com/2021/05/dummy-website.html')
driver.maximize_window()
driver.implicitly_wait(15)
list_elements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for elem in list_elements:
    time.sleep(1)
    elem.click()
#list_elements[1].click()
#list_elements[5].click()
time.sleep(2)
driver.close()


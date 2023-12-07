from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get('https://automationbysqatools.blogspot.com/2021/05/dummy-website.html')
driver.maximize_window()
driver.implicitly_wait(15)
# scroll the webpage with javascript
"""
driver.execute_script("window.scrollBy(0, 3000)")
"""
time.sleep(10)

# scroll page to specific element
"""
element = driver.find_element(By.XPATH, "//input[@id='postcode']")
action = ActionChains(driver)
action.move_to_element(element)
action.perform()
"""

# scroll into view the element with javascript
time.sleep(5)
element = driver.find_element(By.XPATH, "//input[@id='postcode']")
driver.execute_script("arguments[0].scrollIntoView(true)", element)

time.sleep(10)
driver.close()


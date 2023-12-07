from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

browser = 'firefox'
driver = None

if browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == 'edge':
    driver = webdriver.Edge()

wait = WebDriverWait(driver, 20)


driver.get('https://google.co.in')
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.NAME, "q").send_keys("Python Programming")
element = driver.find_element(By.XPATH, "(//input[@name='btnK'])[1]")
#element = wait.until(ec.element_to_be_clickable((By.XPATH, "(//input[@name='btnK1'])[1]")))
# status = element.is_displayed()
status = element.is_enabled()
print("status :", status)
if status:
    element.click()
time.sleep(5)
driver.close()


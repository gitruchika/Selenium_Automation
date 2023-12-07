from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

#options = webdriver.ChromeOptions()
headless = False
incognito = True

chrome_options = Options()
if headless:
    chrome_options.add_argument("--headless")
if incognito:
    chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://automationbysqatools.blogspot.com/2021/05/dummy-website.html')
driver.maximize_window()
driver.implicitly_wait(15)
male_element = driver.find_element(By.ID, "male")
print("is checked :", male_element.is_selected())
male_element.click()
print("is checked :", male_element.is_selected())
time.sleep(2)

checkbox_elem = driver.find_element(By.XPATH, "//td[text()='6001']//parent::tr//input[@type='checkbox']")
print("checkbox is checked :", checkbox_elem.is_selected())
checkbox_elem.click()
print("checkbox is checked :", checkbox_elem.is_selected())
time.sleep(2)
driver.save_screenshot("C:\\PythonSelenium\\headless_screenshot.png")
driver.close()


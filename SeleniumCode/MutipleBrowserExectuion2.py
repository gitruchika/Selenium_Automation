from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def execute_google_search(browser, search_content):
    driver = browser
    wait = WebDriverWait(driver, 20)
    driver.get('https://google.co.in')
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.find_element(By.NAME, "q").send_keys(search_content)
    #driver.find_element(By.XPATH, "(//input[@name='btnK'])[1]").click()
    element = wait.until(ec.element_to_be_clickable((By.XPATH, "(//input[@name='btnK'])[1]")))
    element.click()
    time.sleep(5)
    driver.close()

browsers_list = [(webdriver.Chrome(), "Python"),
                 (webdriver.Firefox(), "Selenium"),
                 (webdriver.Edge(), "Pytest Framework")]

for data in browsers_list:
    execute_google_search(data[0], data[1])

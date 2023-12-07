from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://collegedunia.com/engineering/indore-colleges")
driver.maximize_window()
driver.implicitly_wait(10)
#element = driver.find_element(By.XPATH, "(//h3[@class='jsx-2393160101 font-weight-medium text-lg mb-0'])[1]")
#print(element.text)
#college_name_links = driver.find_elements(By.XPATH, "//div[contains(@class, 'clg-name-address')]//a[@data-ga-event-category='info']")
college_name_links = driver.find_elements(By.XPATH, "//a[@data-ga-event-category='info']")
for element in college_name_links:
    print(element.get_attribute("data-csm-title"))

time.sleep(5)
driver.close()


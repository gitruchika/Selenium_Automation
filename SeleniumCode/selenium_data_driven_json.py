from selenium import webdriver
from SeleniumCode.utillity import *
from selenium.webdriver.common.by import By
import time


test_data = get_json_data("test_resource_data.json")
excel_data = get_excel_data("test_excel.xlsx", row=1, col=1)
print(test_data)
driver = webdriver.Chrome()
driver.get(test_data['url'])
driver.maximize_window()
driver.implicitly_wait(15)
first_name_element = driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]")
first_name_element.clear()
first_name_element.send_keys(test_data['first_name'])

last_name_element = driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]")
last_name_element.clear()
last_name_element.send_keys(test_data['last_name'])

from_city_elem = driver.find_element(By.ID, "fromcity")
from_city_elem.clear()
from_city_elem.send_keys(test_data['src_city'])

dest_city_elem = driver.find_element(By.ID, "destcity")
dest_city_elem.clear()
dest_city_elem.send_keys(test_data['dest_city'])
driver.find_element(By.XPATH, "//input[@name='departdate']").send_keys("11/15/2023")

billing_name = driver.find_element(By.ID, "billing_name")
billing_name.send_keys(excel_data)

time.sleep(10)
driver.close()


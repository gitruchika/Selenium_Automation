from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('https://automationbysqatools.blogspot.com/2021/05/dummy-website.html')
driver.maximize_window()
driver.implicitly_wait(15)
#select_obj = Select(driver.find_element(By.ID, "admorepass"))
#select_obj.select_by_visible_text("Add 3 more passenger (200%)")
#select_obj.select_by_index(2)
#select_obj.select_by_value("2")

# Select country from dropdown
sel_country = Select(driver.find_element(By.ID, "billing_country"))
sel_country.select_by_visible_text("American Samoa")
driver.save_screenshot("dropdown_selection.png")
time.sleep(5)
driver.close()



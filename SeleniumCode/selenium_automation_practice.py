from selenium import webdriver
from SeleniumCode.utillity import *
from selenium.webdriver.common.by import By
import time


test_data = get_json_data("test_resource_data.json")
print(test_data)
driver = webdriver.Chrome()
driver.get(test_data['url2'])
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//span[text()='From']//parent::div").click()
driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::input").send_keys(test_data['src_loc'])
driver.find_element(By.XPATH, f"//span[contains(text(), '{test_data['src_loc']}')]//ancestor::li").click()
time.sleep(5)
driver.close()






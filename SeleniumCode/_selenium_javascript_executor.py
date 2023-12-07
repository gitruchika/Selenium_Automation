from selenium import webdriver
from test_data import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(timeout)
var1 = driver.execute_script("return document.URL")
print("URL :", var1)
var2 = driver.execute_script("return document.title")
print("Title :", var2)


driver.get("https://www.goibibo.com")
time.sleep(5)
links = driver.execute_script("return document.links")
print(links)
for link in links:
    print(link.text)

driver.close()
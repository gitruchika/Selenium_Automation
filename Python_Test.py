# var1 = "Manish"
#
# print(var1[::-1])
#
# output = ''
# for i in range(-1, -len(var1)-1, -1):
#     output = output + var1[i]
#
# print(output)
#
# from datetime import datetime, timedelta
# import time
# print(datetime.now())
# print(time.time())

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browsers = ['Chrome', 'Firefox']
driver = None
for browser in browsers: 
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://google.co.in")

    driver.find_element(By.NAME, "q").send_keys("Python")
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)
    driver.save_screenshot("google_page.png")

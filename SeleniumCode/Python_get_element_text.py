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
college_name_list = driver.find_elements(By.XPATH, "//h3[@class='jsx-2393160101 font-weight-medium text-lg mb-0']")
college_fee_list = driver.find_elements(By.XPATH, "//a[@data-ga-event-category='courses-fees']/span[1]")
college_review = driver.find_elements(By.XPATH, "//a[@data-ga-event-category='reviews']/span[1]")
for i in range(len(college_name_list)):
    print(i+1, ":", college_name_list[i].text, "|", college_fee_list[i].text, "|", college_review[i].text)
    print("_"*100)

time.sleep(5)
driver.close()


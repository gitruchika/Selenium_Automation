from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

"""
implicit wait : This wait apply on the all the elements of the web page.
explicit wait : This wait apply on the specific element on specific condition.
static wait : this wait, hard coded, once it is apply then we have to wait till the time has defined.


"""

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://collegedunia.com/engineering/indore-colleges")
driver.maximize_window()
driver.implicitly_wait(10)
#element = driver.find_element(By.XPATH, "(//h3[@class='jsx-2393160101 font-weight-medium text-lg mb-0'])[1]")

element = wait.until(ec.visibility_of_element_located((By.XPATH, "(//h3[@class='jsx-2393160101 font-weight-medium text-lg mb-0'])[1]")))
element.click()

time.sleep(5)  #static wait
driver.close()


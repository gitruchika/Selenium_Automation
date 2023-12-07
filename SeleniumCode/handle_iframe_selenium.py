from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/')
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID, "iFrame").click()
time.sleep(3)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='globalSqa']"))
time.sleep(3)
#driver.find_element(By.ID, "mobile_menu_toggler").click()
#driver.find_element(By.XPATH, "(//a[text()='Home' and @aria-current='page'])[2]//parent::li").click()
phone_number = driver.find_element(By.XPATH, "//div[@class='header_phone']").text
print(phone_number)
email = driver.find_element(By.XPATH, "//div[@class='header_mail']").text
print(email)
time.sleep(3)

driver.switch_to.default_content()
driver.find_element(By.XPATH, "//li[@id='menu-item-6898']//a[text()='CheatSheets']").click()
time.sleep(5)
driver.close()



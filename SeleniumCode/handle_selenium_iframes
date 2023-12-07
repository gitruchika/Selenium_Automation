from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('https://automationbysqatools.blogspot.com/p/manual-testing.html')
driver.maximize_window()
driver.implicitly_wait(15)

# clicking on blackbox testing linking on first tab
current_tab = driver.current_window_handle

driver.find_element(By.XPATH, "//a[contains(text(),'Grey Box Testing')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Unit Testing ')]").click()
# The black box testing article will open in a new tab.
time.sleep(2)
# Now there are two browser windows, here will list of tabs address
all_windows = driver.window_handles
print("all windows :", all_windows)
driver.switch_to.window(all_windows[1])
time.sleep(2)
#header = driver.find_element(By.XPATH, "//h3[@itemprop=name]")
#print("second tab :", header.text)
driver.find_element(By.NAME, "q").send_keys("Python")

driver.close()

driver.switch_to.window(all_windows[2])
time.sleep(2)
#header = driver.find_element(By.XPATH, "//h3[@itemprop=name]")
#print("Third tab :", header.text)
driver.find_element(By.NAME, "q").send_keys("Programming")
time.sleep(5)
driver.close()


driver.switch_to.window(all_windows[0])

driver.find_element(By.XPATH, "//div[@class='widget-content']//a[contains(text(), 'Home')]").click()
time.sleep(5)

driver.close()



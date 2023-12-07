from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('https://automationbysqatools.blogspot.com/p/manual-testing.html')
driver.maximize_window()
driver.implicitly_wait(15)

# clicking on blackbox testing linking on first tab
driver.find_element(By.XPATH, "//a[contains(text(),'Black Box Testing')]").click()
# The black box testing article will open in a new tab.

# Now there are two browser windows, here will list of tabs address
all_windows = driver.window_handles

print(all_windows)
time.sleep(2)

driver.switch_to.window(all_windows[1])
# Switch to new browser tab.


# Verify header at new windows tab opened.
element = driver.find_element(By.XPATH, "//h3[contains(text(),'Black Box Testing')]")
assert element
time.sleep(2)

# close to new browser tab.
driver.close()

time.sleep(2)
# Switch to parent browser windows.
driver.switch_to.window(all_windows[0])
time.sleep(2)
# click on Home Menu Option.
driver.find_element(By.XPATH, "//div[@class='widget-content']//a[contains(text(), 'Home')]").click()
time.sleep(2)

# close the browser.
driver.close()



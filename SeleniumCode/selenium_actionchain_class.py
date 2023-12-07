from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
driver.maximize_window()
driver.implicitly_wait(15)

# Mouse Hover Action
"""
element = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='Free Ebooks']")
action = ActionChains(driver)
action.move_to_element(element)
action.perform()
time.sleep(5)
"""

# Drag and Drop
"""
frame_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(frame_element)
image1_element = driver.find_element(By.XPATH, "//img[@alt='The chalet at the Green mountain lake']//parent::li")
trash_element = driver.find_element(By.XPATH, "//div[@id='trash']")

action = ActionChains(driver)
action.drag_and_drop(image1_element, trash_element)
action.perform()

time.sleep(5)
driver.switch_to.default_content()
"""

# context click with Actions chain.

element = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='Free Ebooks']")
action = ActionChains(driver)
action.context_click(element)
action.perform()
time.sleep(10)

driver.close()
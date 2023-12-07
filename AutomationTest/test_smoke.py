import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from AutomationTest.data_file import *
from utils import get_json_data

jd = get_json_data()


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)

@pytest.mark.parametrize("browser, search", [(webdriver.Chrome(), jd['search1']),
                                             (webdriver.Firefox(), jd['search2']),
                                             (webdriver.Edge(), jd['search3'])])
def test_search_data_on_google(browser, search):
    driver = browser
    driver.implicitly_wait(20)
    driver.get(url)
    driver.find_element(By.NAME, "q").send_keys(search)
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)
    driver.save_screenshot("google_page.png")

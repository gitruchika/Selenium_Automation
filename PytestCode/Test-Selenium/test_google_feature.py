import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


@pytest.mark.parametrize("search_value", ["Python", "Cricket worldcup 2023", "FiFa world cup"])
def test_search_google_data(setup, search_value):
    setup.get("https://www.google.co.in")
    setup.find_element(By.NAME, "q").send_keys(search_value)
    setup.find_element(By.NAME, "btn").click()
    time.sleep(3)


